import os
from distutils import dir_util

anonymous_dict = {}

def import_anonymous_users():
    anonymous_filename = '/home/david/s3_oa_courses/oa_courses.csv'

    with open(anonymous_filename, 'r') as fp:
        for i in range(1):
            next(fp)

        for line in fp:
            # fields[0] = anonymous_user_id
            # fields[1] = username
            fields = [field for field in line.split(',')]
            anonymous_dict[fields[0]] = fields[1]

def parse_s3_dump():
    root_dir = '/home/david/s3_oa_dump/prod'
    output_dir = '/home/david/s3_ora_results'

    for subdir, dirs, files in os.walk(root_dir):
        for dir in dirs:
            if dir in anonymous_dict:
                source_dir =  os.path.join(root_dir, dir)
                target_dir =  os.path.join(output_dir, anonymous_dict[dir])
                print(source_dir, target_dir)

                dir_util.copy_tree(source_dir, target_dir)

def main():
    import_anonymous_users()
    parse_s3_dump()

if __name__ == "__main__":
    main()