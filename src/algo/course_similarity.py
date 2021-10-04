import numpy as np
import pandas as pd

import src.algo.docsim as docsim


def course_sim(query):
    data = pd.read_csv("resources/processed_data/processed_data.tsv", sep='\t')
    data = data.groupby("course_id").agg(
        {'course_name_x': 'first', 'course_desc': 'first', 'units_y': 'first', 'College': 'first',
         'Total # Students': np.mean, '# Responses': np.mean, 'Hrs Per Week': np.mean,
         'Interest in student learning': np.mean, 'Clearly explain course requirements': np.mean,
         'Clear learning objectives & goals': np.mean, 'Instructor provides feedback to students to improve': np.mean,
         'Demonstrate importance of subject matter': np.mean, 'Explains subject matter of course': np.mean,
         'Show respect for all students': np.mean, 'Overall teaching rate': np.mean, 'Overall course rate': np.mean})

    docsim_obj = docsim.DocSim(verbose=True)
    similarities = docsim_obj.similarity_query(query, data["course_desc"] + data["course_name_x"])
    for idx, score in (sorted(enumerate(similarities), reverse=True, key=lambda x: x[1])):
        print(f'{score:0.3f} \t {data.iloc[idx]["course_name_x"]}')


if __name__ == '__main__':
    course_sim("Machine Learning")
