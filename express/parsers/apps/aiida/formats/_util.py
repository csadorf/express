import errno
import json
import os
import uuid
import zipfile

import click
import esse
import jsonschema
import tqdm
from datetime import datetime, tzinfo, timedelta


SUPPORTED_ARCHIVE_VERSION = '0.9'
SUPPORTED_AIIDA_VERSION = '1.4.2'

ES = esse.ESSE()
SCHEMA_MATERIAL = ES.get_schema_by_id('material')


def parse_structure_node_attributes(export_data, attributes):
    """Parse an AiiDA StructureData node."""
    # Prepare mapping
    assert export_data['node_type'] == 'data.structure.StructureData.'

    sites = list(enumerate(attributes['sites']))
    kinds = {kind['name']: kind for kind in attributes['kinds']}
    assert all(len(kind['symbols']) == 1 for kind in kinds.values())

    instance = {
        'schemaVersion':  '0.2.0',

        # TODO: THE FOLLOWING VARIABLES ARE PLACEHOLDERS!
        '_id': export_data['uuid'],
        'exabyteId': 'PLACEHOLDER',
        'hash': 'PLACEHOLDER',

        # TODO: Gather from export data?
        'creator': 'CREATOR',
        'owner': 'OWNER',

        # THE FOLLOWING ATTRIBUTES SHOULD BE IMPROVED:
        'created_at': export_data['ctime'],  # TODO: or maybe mtime?

        # Actual materials-related data
        'lattice': {
            'vectors': {
                'a': attributes['cell'][0],
                'b': attributes['cell'][1],
                'c': attributes['cell'][2],
            }
        },
        'basis': {
            'elements': [{'id': _id, 'value': kinds[site['kind_name']]['name']} for _id, site in sites],
            'coordinates': [{'id': _id, 'value': site['position']} for _id, site in sites],
        },
    }

    # Validate result and return
    ES.validate(instance, schema=SCHEMA_MATERIAL)
    return instance


def parse_aiida_archive_file(path):
    """Parse an AiiDA archive file located at path."""
    with zipfile.ZipFile(path) as source:
        metadata = json.loads(source.read('metadata.json'))
        data = json.loads(source.read('data.json'))

        # version check
        assert metadata['aiida_version'] == SUPPORTED_AIIDA_VERSION
        assert metadata['export_version'] == SUPPORTED_ARCHIVE_VERSION

        # gather structure nodes
        nodes = data['export_data']['Node']
        structure_nodes = {pk: node for (pk, node) in nodes.items()
                           if node['node_type'] == 'data.structure.StructureData.'}
        click.echo("# number of structure nodes: {}".format(len(structure_nodes)))

        for pk in tqdm.tqdm(structure_nodes, desc='parsing structure nodes'):
            export_data = data['export_data']['Node'][pk]
            node_attributes = data['node_attributes'][pk]
            yield parse_structure_node_attributes(export_data, node_attributes)



@click.command(
    help="""convert AiiDA export archive files to esse",

    The aiida-to-esse tool analyzes an AiiDA export archive
    file for data nodes that can be translated into valid
    esse files and then performs that translation.""")
@click.argument(
    'source_file',
    nargs=-1,
    type=click.Path(
        exists=True,
        dir_okay=False,
        ),
    )
@click.argument(
    'target_directory',
    type=click.Path(
        exists=False,
        file_okay=False,
        dir_okay=True,
        writable=True,
        ),
    )
@click.option(
    '--skip-errors',
    help="Continue when encountering errors.",
    is_flag=True,
    )
def main(source_file, target_directory, skip_errors):
    try:
        os.makedirs(target_directory)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise

    for path_source in source_file:
        click.echo("Parsing {!r}...".format(path_source))
        for material in parse_aiida_archive_file(path_source):
            # Generate output filename
            fn_out = os.path.join(target_directory, '{}.json'.format(material['_id']))

            # Serialize to JSON
            blob = json.dumps(material, encoding='utf-8')

            # Check if file exists and is non-empty
            try:
                stat = os.stat(fn_out)
                assert stat.st_size > 0
            except OSError as error:
                if error.errno == errno.ENOENT:
                    pass
            else:
                continue  # file already exists and is non-empty, skip

            # TODO: Consider to write to temporary file first.
            with open(fn_out, 'wb') as outfile:
                outfile.write(blob)
