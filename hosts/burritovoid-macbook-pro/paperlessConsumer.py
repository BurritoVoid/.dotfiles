import datetime
import os
import shutil

scanner_inbox_path = '/Users/burritovoid/Nextcloud/documents/0-scanner-inbox'
paperless_inbox_path = '/Volumes/paperless-consumer'
storage_path = "/Users/burritovoid/Nextcloud/documents/zzz-pre-paperless-archive"

now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

valid_extensions = ['pdf', 'jpeg', 'jpg', 'txt']

# Check that all needed paths exist:

for path in [scanner_inbox_path, paperless_inbox_path, storage_path]:
    if not os.path.exists(path):
        print('Required path not found: ' + path)
        print('Exiting.')
        exit()

inbox_list = os.listdir(scanner_inbox_path)
files_processed_count = 0
files_skipped_count = 0

for item in inbox_list:
    # print(item)
    if os.path.isdir(scanner_inbox_path + '/' + item):
        print(item + ' is a directory. Skipping.')
        files_skipped_count += 1
        continue
    file_parts = item.split('.')
    if file_parts[-1].lower() in valid_extensions:
        file_source_string = scanner_inbox_path + '/' + item
        file_copy_target = paperless_inbox_path + '/' + item
        file_move_target = storage_path + '/' + now + '-' + item

        # Copy the file to the paperless inbox:
        try:
            shutil.copy(file_source_string, file_copy_target)

            # shutil.copy(file_source_string, file_move_target)
            shutil.move(file_source_string, file_move_target)
        
        except shutil.SameFileError:
            print("Source and destination represents the same file.")
        # If there is any permission issue
        except PermissionError:
            print("Permission denied.")
        # For other errors
        except:
            print("Error occurred while copying file.")
        files_processed_count += 1

        # print(file_source_string)
        # print(file_copy_target)
        # print(file_move_target)
    else:
        # don't bother notifying about ds_store
        if item != '.DS_Store':
            print(item + ' is not a recognized filetype. Skipping')
            files_skipped_count += 1

print(str(files_processed_count) + ' files ingested, ' + str(files_skipped_count) + ' items skipped.')