import os

def new_post(week_number,  picture, poster_text_file='new_poster_text.txt'):
    """
    enter week number as number (above 12) or written with a captital letter

    enter the file name for the picture (and path if not in the same dir)
    
    enter file name of file with the corresponding text, only in one line, 
    or delete the first line of the existing file and write it there
    """

    end = "    <!-- toilet data end -->"

    with open(poster_text_file, 'r') as t:
        poster_text=t.read()

    with open("poster_template.txt", 'rt') as t:
        template = t.read()

        template = template.replace('WEEK_NUMBER', str(week_number))
        template = template.replace('PLACEHOLDER_POSTER_TEXT', poster_text)
        template = template.replace('PLACEHOLDER_PIC', picture)

    if input(f"Are you sure you want to add Week {week_number} with the picture {picture} and the following text below to the poster data side?\n[y/n] \n\n{poster_text}\n") == 'y':

        with open("index.html", "rt") as fin:
            with open("out.html", "wt") as fout:
                for line in fin:
                    fout.write(line.replace(end, template))
        
        os.remove("index.html")
        os.rename("out.html", "index.html")
    else: 
        print("Action cancelled.")


new_post(week_number='Eight', poster_text_file='new_poster_text.txt', picture='results_week8.png')
    