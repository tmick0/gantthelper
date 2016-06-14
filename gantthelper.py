import dateutil, dateutil.parser
from itertools import chain, count, cycle

DEFAULT_COLORS = [
    "Apricot", "Bittersweet",
    "Blue", "Cerulean", "DarkOrchid",
    "ForestGreen", "Goldenrod", "OrangeRed",
    "RedOrange", "Rhodamine", "SpringGreen",
    "YellowGreen"
]

class TaskDefinition (object):
    
    def __init__(self, name, start_date, end_date, assigned_to=None):
        self.name        = name
        self.start_date  = dateutil.parser.parse(start_date)
        self.end_date    = dateutil.parser.parse(end_date)
        self.assigned_to = assigned_to

class GanttDefinition (object):
    
    def __init__(self, dictionary=None):
        self._groups = {}
        if dictionary is not None:
            self.load(dictionary)
        
    def load(self, dictionary):
        for group, tasks in dictionary.items():
            if not group in self._groups:
                self._groups[group] = []
            for task in tasks:
                self._groups[group].append(TaskDefinition(**task))
    
    def _group_min(self, group):
        return min(task.start_date for task in group)
    
    def _group_max(self, group):
        return max(task.end_date for task in group)
    
    def get_groups(self):
        return [
            (   group,
                self._group_min(tasks),
                self._group_max(tasks),
                sorted(tasks, key=lambda x: x.start_date)
            )
            for group, tasks in sorted(
                self._groups.items(),
                key=lambda x: self._group_min(x[1])
            )
        ]
    
    def get_start(self):
        return min(self._group_min(v) for v in self._groups.values())
    
    def get_end(self):
        return max(self._group_max(v) for v in self._groups.values())

    def get_names(self):
        names = set()
        for tasks in self._groups.values():
            names |= set([x.assigned_to for x in tasks if x.assigned_to is not None])
        return sorted(names)

def _iso_date_list(*args):
    return map(lambda x: x.strftime("%Y-%m-%d"), args)

def generate_tex_preamble(gantt, colors=None):
    if colors is None:
        colors = DEFAULT_COLORS
        
    print("""\
\\documentclass[border=4pt]{standalone}
\\usepackage[usenames,dvipsnames,svgnames]{xcolor}
\\usepackage{pgfgantt}
\\usetikzlibrary{positioning}
\\usetikzlibrary{backgrounds}
\\tikzstyle{unassigned}=[] \
""")
    
    for idx, name, color in zip(count(), gantt.get_names(), cycle(colors)):
        print("\\tikzstyle{%s}=[fill=%s]" % ("name_%d" % idx, color))
    
    print("")
    
def generate_tex_gantt(gantt):
    start_date = gantt.get_start()
    end_date   = gantt.get_end()
    
    key = {v: i for i, v in enumerate(gantt.get_names())}
    
    print("""
    \\begin{ganttchart}[
        x unit=0.6125cm,
    	y unit chart=0.5cm,
    	hgrid=true,
    	vgrid=true,
    	time slot format=isodate
    ]{%s}{%s}

    \gantttitlecalendar{month=name, day}
    """ % tuple(_iso_date_list(start_date, end_date)))
    
    for group, start, end, tasks in gantt.get_groups():
    
        print("""
        \\\\\\ganttgroup{%s}
        {%s}{%s}
        """ % tuple(chain([group], _iso_date_list(start, end))))
        
        for task in tasks:
        
            print("""
            \\\\\\ganttbar[bar/.append style=%s]
            {%s}
            {%s}{%s}
            """ % tuple(chain(
                [
                    ("name_%d" % key[task.assigned_to])
                    if task.assigned_to is not None
                    else "unassigned",
                    
                    task.name
                ],
                _iso_date_list(task.start_date, task.end_date)
            )))
            
    
        print("""
        \\\\
        """)
    
    print("""
    \\end{ganttchart}
    """)

def generate_tex_key(gantt):
    print("""
    \\hspace{0.125in}
    \\begin{tikzpicture}[framed,scale=0.8,every node/.style={transform shape}]
    \\node (kh) [] {\\textbf{Key}};
    """)
    
    last = "kh"
    names = gantt.get_names()
    
    for idx in range(len(names)+1):
        print("\\node (%s) [below=0.125in of %s, %s, rectangle,draw,minimum width=1in]{};" %(
            "b%d" % idx,
            last,
            ("name_%d" % idx) if idx < len(names) else "unassigned"
        ))
        last = "b%d" % idx
    
    for idx in range(len(names)+1):
        print("\\node (%s) [right=0.125in of %s]{%s};" %(
            "l%d" % idx,
            "b%d" % idx,
            (names[idx]) if idx < len(names) else "Unassigned"
        ))
    
    print("\\end{tikzpicture}\n")

def generate_tex_document(gantt, preamble_args={}):
    generate_tex_preamble(gantt, **preamble_args)
    print("\\begin{document}\n")
    generate_tex_gantt(gantt)
    generate_tex_key(gantt)
    print("\\end{document}\n")
