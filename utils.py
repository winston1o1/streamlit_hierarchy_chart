import pandas as pd

def cx_credit_mtree(df:pd.DataFrame,main_dt,comparator_dt):
    '''
    Args:
        df: pandas dataframe,
        main_dt: The date with the focus values
        comparator_dt: 
    Returns:
        dict with a structure:
            template = {
                'key':'0',
                'label': 'Metric',
                'value': '0',
                'comparator': '0',
                'styleClass': 'class',
                'children':[]
            }
    '''
    
    main_df = df[df['month']==main_dt]
    comparator_df = df[df['month']==comparator_dt]

    main_total_calls = int(main_df['total_calls'].iloc[0])
    main_answered_calls = int(main_df['answered'].iloc[0])
    main_answered_per_person = int(main_df['avg_answered_per_agent'].iloc[0])
    main_answered_agents_total = int(main_df['total_agents_answered'].iloc[0])
    main_overachiever = int(main_df['overachiever'].iloc[0])
    main_underachiever = int(main_df['underachiever'].iloc[0])

    main_missed_calls = int(main_df['missed'].iloc[0])
    main_missed_out_working_hrs = int(main_df['missed_out_of_working_hours'].iloc[0])
    main_missed_in_working_hrs = int(main_df['missed_in_of_working_hours'].iloc[0])

    comparator_total_calls = int(comparator_df['total_calls'].iloc[0])
    comparator_answered_calls = int(comparator_df['answered'].iloc[0])
    comparator_answered_per_person = int(comparator_df['avg_answered_per_agent'].iloc[0])
    comparator_answered_agents_total = int(comparator_df['total_agents_answered'].iloc[0])
    comparator_overachiever = int(comparator_df['overachiever'].iloc[0])
    comparator_underachiever = int(comparator_df['underachiever'].iloc[0])

    comparator_missed_calls = int(comparator_df['missed'].iloc[0])
    comparator_missed_out_working_hrs = int(comparator_df['missed_out_of_working_hours'].iloc[0])
    comparator_missed_in_working_hrs = int(comparator_df['missed_in_of_working_hours'].iloc[0])


    mtree = {
        'key':'0',
        'label': 'Inbound Calls',
        'value': main_total_calls,
        'comparator': comparator_total_calls,
        'styleClass': 'bg-success' if main_total_calls > comparator_total_calls else 'bg-danger',
        'children':[]
    }
    level_2_answered = {
                'key':'0_1',
                'label': 'Answered',
                'value': f'Calls: {main_answered_calls} ({main_answered_calls/main_total_calls :.0%})',
                'comparator': f'Calls: {comparator_answered_calls} ({comparator_answered_calls/comparator_total_calls :.0%})',
                'styleClass': 'bg-success' if main_answered_calls > comparator_answered_calls else 'bg-danger',
                'children':[
                ]
            }

    level_2_missed = {
                'key':'0_2',
                'label': 'Missed',
                'value': f'Calls: {main_missed_calls} ({main_missed_calls/main_total_calls :.0%})',
                'comparator': f'Calls: {comparator_missed_calls} ({comparator_missed_calls/comparator_total_calls :.0%})',
                'styleClass': 'bg-success' if main_missed_calls < comparator_missed_calls else 'bg-danger',
                'children':[
                ]
            }

    level_3_answered_avg_person = {
                'key':'0_1_1',
                'label': 'Avg Per Agent',
                'value': f'{main_answered_per_person} ({main_answered_agents_total} agents)',
                'comparator': f'{comparator_answered_per_person}({comparator_answered_agents_total} agents)',
                'styleClass': 'bg-success' if main_answered_per_person > comparator_answered_per_person else 'bg-danger',
                'children':[
                ]
            }

    level_3_missed_in_working_hrs = {
                'key':'0_2_1',
                'label': 'In Hrs',
                'value': f'Calls: {main_missed_in_working_hrs} ({main_missed_in_working_hrs/main_missed_calls :.0%})',
                'comparator': f'Calls: {comparator_missed_in_working_hrs} ({comparator_missed_in_working_hrs/main_missed_calls :.0%})',
                'styleClass': 'bg-success' if main_missed_in_working_hrs < comparator_missed_in_working_hrs else 'bg-danger',
            }

    level_3_missed_out_working_hrs = {
                'key':'0_2_2',
                'label': 'Off Hrs',
                'value': f'Calls: {main_missed_out_working_hrs} ({main_missed_out_working_hrs/main_missed_calls :.0%})',
                'comparator': f'Calls: {comparator_missed_out_working_hrs} ({comparator_missed_out_working_hrs/main_missed_calls :.0%})',
                'styleClass': 'bg-success' if main_missed_out_working_hrs < comparator_missed_out_working_hrs else 'bg-danger',
            }

    level_4_answered_avg_person_overperformers = {
                'key':'0_1_1_1',
                'label': 'Overachievers',
                'value': f'{main_overachiever} agents',
                'comparator': f'{comparator_overachiever} agents',
                'styleClass': 'bg-success' if main_overachiever > comparator_overachiever else 'bg-danger',
            }

    level_4_answered_avg_person_underperformers = {
                'key':'0_1_1_2',
                'label': 'Underachievers',
                'value': f'{main_underachiever} agents',
                'comparator': f'{comparator_underachiever} agents',
                'styleClass': 'bg-success' if main_underachiever > comparator_underachiever else 'bg-danger',
            }
    
    mtree['children'].append(level_2_answered)
    mtree['children'].append(level_2_missed)
    mtree['children'][0]['children'].append(level_3_answered_avg_person)
    mtree['children'][0]['children'][0]['children'].append(level_4_answered_avg_person_overperformers)
    mtree['children'][0]['children'][0]['children'].append(level_4_answered_avg_person_underperformers)
    mtree['children'][1]['children'].append(level_3_missed_in_working_hrs)
    mtree['children'][1]['children'].append(level_3_missed_out_working_hrs)

    metric_key_dict = {
        '0':'total_calls',
        '0_1':'answered',
        '0_1_1':'avg_answered_per_agent',
        '0_1_1_1':'overachiever',
        '0_1_1_2':'underachiever',
        '0_2':'missed',
        '0_2_1':'missed_in_of_working_hours',
        '0_2_2':'missed_out_of_working_hours',
    }

    return mtree, metric_key_dict
