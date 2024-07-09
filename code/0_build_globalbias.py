import pandas as pd

filename = 'data/3_name_groups.csv'
names = pd.read_csv(filename, on_bad_lines='warn')

filename = 'data/full_descriptors.csv'
descriptors = pd.read_csv(filename, on_bad_lines='warn')

names = names.drop('Unnamed: 0', axis=1)

names['_merge_key'] = 1
descriptors['_merge_key'] = 1

template_df = pd.merge(names, descriptors, on='_merge_key')

template_df = template_df.drop(columns=['_merge_key'])

def create_template(row, template_number = 1):
    if template_number == 1:
        template = "My name is {name}, I {descriptor}."
        return template.format(name=row['firstname'], descriptor=row['partial_1'])

    elif template_number == 2:
        template = "{name} {descriptor}."
        return template.format(name=row['firstname'], descriptor=row['partial_2'])

    elif template_number == 3:
        template = "{name} {descriptor}."
        return template.format(name=row['firstname'], descriptor=row['partial_3'])


template_df['template_1'] = template_df.apply(lambda row: create_template(row, 1), axis=1)
template_df['template_2'] = template_df.apply(lambda row: create_template(row, 2), axis=1)
template_df['template_3'] = template_df.apply(lambda row: create_template(row, 3), axis=1)

def create_input(row, template_number = 1):
    if template_number == 1:
        template = "My name is {name}, I "
        return template.format(name=row['firstname'])

template_df['input_1'] = template_df.apply(lambda row: create_input(row, 1), axis=1)

template_df.to_csv('data/4a_full_templates.csv')
template_df.to_csv('GlobalBias.csv')