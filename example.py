from gantthelper import GanttDefinition, generate_tex_document

colors = [
    "JungleGreen",
    "RedOrange",
    "Dandelion"
]

taskdefs = {

    "Task Group 1": [
        {   "name":         "Task 1",
            "start_date":   "June 20",
            "end_date":     "June 26",
            "assigned_to":  "Alice"
        },
        
        {   "name":         "Task 2",
            "start_date":   "June 27",
            "end_date":     "June 30",
            "assigned_to":  "Alice"
        },
        
        {   "name":         "Task 3",
            "start_date":   "June 20",
            "end_date":     "June 27",
            "assigned_to":  "Bob"
        }
    ],
    
    "Task Group 2": [
        {   "name":         "Task 4",
            "start_date":   "June 28",
            "end_date":     "July 11",
            "assigned_to":  "Bob",
        },
        
        {   "name":         "Task 5",
            "start_date":   "July 1",
            "end_date":     "July 15",
            "assigned_to":  "Alice"
        }
    ],
    
    "Task Group 3": [
        {   "name":         "Task 6",
            "start_date":   "June 30",
            "end_date":     "July 5",
            "assigned_to":  "Charlie"        
        },
        
        {   "name":         "Task 7",
            "start_date":   "June 30",
            "end_date":     "July 11"
        }
    ],
    
    "Task Group 4": [
        {   "name":         "Task 8",
            "start_date":   "July 6",
            "end_date":     "July 13",
            "assigned_to":  "Charlie"
        },
        
        {   "name":         "Task 9",
            "start_date":   "July 12",
            "end_date":     "July 25"
        },
        
        {   "name":         "Task 10",
            "start_date":   "July 14",
            "end_date":     "July 25",
            "assigned_to":  "Charlie"
        },
        
        {   "name":         "Task 11",
            "start_date":   "July 16",
            "end_date":     "July 25",
            "assigned_to":  "Alice"
        }
    ],
    
    "Task Group 5": [
        {   "name":         "Task 12",
            "start_date":   "July 16",
            "end_date":     "July 25",
            "assigned_to":  "Bob"
        },
        
        {   "name":         "Task 13",
            "start_date":   "July 26",
            "end_date":     "August 4",
            "assigned_to":  "Charlie"
        },
        
        {   "name":         "Task 14",
            "start_date":   "August 5",
            "end_date":     "August 12"
        }
    ]

}

gantt = GanttDefinition(taskdefs)

generate_tex_document(gantt, preamble_args={'colors': colors})
