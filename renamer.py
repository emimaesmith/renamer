import datetime
import json
import logging
import ntpath
import os
import random
import shutil
import sys

log = logging.getLogger()
log.setLevel(10)
consoleHandler = logging.StreamHandler(sys.stdout)
log.addHandler(consoleHandler)

if __name__ == '__main__':
   argv = sys.argv
   if argv is None:
      log.error('No inputs passed to renamer job')
      sys.exit(1)
   argc = len(argv) - 1
   # Input first file
   input_file = argv[1]
   # Output second file
   output_dir = argv[2]
   # Optional input third file
   if argc == 3:
      optional_input = argv[3]
      log.info('Got the optional input: %s', optional_input)

   log.info('Input_file: %s' % input_file)
   log.info('Output_dir: %s' % output_dir)

   fname = ntpath.basename(input_file)
   old_name = os.path.splitext(fname)
   new_name = old_name[0] + '_RENAMED' + old_name[1]
   output_file = os.path.join(output_dir, new_name)
   output_obj = open(output_file, 'w+')
   output_obj.close()

   log.info('Copying file from %s to %s' % (input_file, output_dir))
   try:
      shutil.copyfile(input_file, output_file)
   except Exception as e:
      log.info('Error copying file: %s' % str(e))
      exit(3)
   log.info('Successfully copied file')

   log.info('Creating results manifest')
   json_dict = {'version': '1.1'}
   json_dict['output_data'] = []
   output_dict = {}
   output_dict['name'] = 'renamed_file'
   output_dict['file'] = {}
   output_dict['file']['path'] = output_file
   output_dict['file']['geo_metadata'] = {}
   output_dict['file']['geo_metadata']['data_started'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
   output_dict['file']['geo_metadata']['data_ended'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
   json_dict['output_data'].append(output_dict)
   parse_results = {'filename': fname}
   parse_results['data_types'] = [random.choice(['hello', 'goodbye', 'aloha'])]
   parse_results['geo_metadata'] = {}
   parse_results['geo_metadata']['data_started'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
   parse_results['geo_metadata']['data_ended'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
   parse_results['geo_metadata']['source_started'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')
   parse_results['geo_metadata']['source_ended'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')
   json_dict['parse_results'] = parse_results

   metadata_dict = {
      'type': 'Feature',
      'geometry': {
         'type': 'Point',
         'coordinates': [0, 0]
      },
      'properties': {
         'dataStarted': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
         'dataEnded': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
      }
   }

   with open(os.path.join(output_dir, 'results_manifest.json'), 'w+') as fout:
      json_string = json.dumps(json_dict)
      fout.write(json_string)
   log.info('Successfully created results manifest')

   with open(os.path.join(output_dir, fname + '.metadata.json'), 'w+') as fout:
      metadata_string = json.dumps(metadata_dict)
      fout.write(metadata_string)
   log.info('Successfully created %s.metadata.json', fname)

   # with open(os.path.join(output_dir, 'seed.outputs.json'), 'w+') as fout:
   #    output_dict={}
   #    output_dict['output'] = random.choice(['hello', 'goodbye', 'aloha'])
   #    json_string = json.dumps(output_dict)
   # log.info('Successfully created seed.outputs.json')