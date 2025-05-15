# This module contains helper functions to support reading and writing to result files
import os


# Each website that crawled is a separate project/folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)


# Create queue and crawled files
# project_name: project name, base url: homepage link
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file and write data
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Read a file and add filenames to set
def file_to_set(filename):
    results = set()
    with open(filename, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results


# Remove old infos and update
def set_to_file(links, filename):
    delete_file_contents(filename)
    for link in links:
        append_to_file(filename, link)


# delete the file contents
def delete_file_contents(filename):
    with open(filename, 'w'):
        pass


# append data to the file
def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')