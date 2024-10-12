# Imports 
import dash_bootstrap_components as dbc

# Initialize factor list
factors = ["Loss of interest", "Feeling down", "Stress", "Worry", "Overthinking", "Sleep problems", 
           "Joint pain", "Changes in appetite", "Self-blame", "Trouble concentrating", "Procrastinating", 
           "Breakup", "Problems at work", "Interpersonal problems"]

# Initialize node color schemes
node_color = ["Uniform", "Severity", "Severity (abs)", "Out-degree", "In-degree", "Out-/In-degree ratio"]

# Initialize node sizing schemes
node_size = ["Uniform", "Severity", "Severity (abs)", "Out-degree", "In-degree", "Out-/In-degree ratio"] 

# Stylesheet
stylesheet = [{'selector': 'node','style': {'background-color': '#9CD3E1', 'label': 'data(label)', 'font-family': 'Arial'}},
              {'selector': 'edge','style': {'curve-style': 'bezier', 'target-arrow-shape': 'triangle', 'control-point-step-size': '40px' }}
    ]

# Initialize styles (buttons)
hidden_style = {'display': 'none'}
visible_style = {'display': 'block', "color": "#8793c9"}

# Dictionary
translations = {
    'en': {
        'welcome_01': 'Welcome to PsySys',
        'welcome_02': 'Dive into your mental health!',
        'video_link_intro': "https://www.youtube.com/embed/d8ZZyuESXcU?si=CYvKNlf17wnzt4iGrel=0&modestbranding=1",
        'title_block_01': 'Everybody struggles from time to time',
        'description_block_01': 'Learn about the variability & identify your personal factors',
        'title_block_02': 'Seeing the connections',
        'description_block_02': 'Learn how your factors influence each other',
        'placeholder_dd_02': "Select your factors that are causally connected",
        'title_block_03': 'Vicious cycles',
        'description_block_03': 'Understand why you might drift into a downward spiral',
        'title_block_04': 'Breaking out of the cycle',
        'description_block_04': 'Detect promising areas for positive change',
        'video_link_block_01': 'https://www.youtube.com/embed/ttLzT4U2F2I?si=xv1ETjdc1uGROZTo',
        'placeholder_dd_01': "Select your personal factors",
        'video_link_block_02': 'https://www.youtube.com/embed/stqJRtjIPrI?si=1MI5daW_ldY3aQz3',
        'placeholder_dd_02': "Select your factors that are causally connected",
        'example_block_02': ('Example: If you feel that normally worrying causes you to become less concentrated, ' 
                             'select these factors in this order.'),
        'video_link_block_03': 'https://www.youtube.com/embed/EdwiSp3BdKk?si=TcqeWxAlGl-_NUfx',
        'placeholder_dd_03': "Select your factors that reinforce each other",
        'example_block_03': ('Example: If you feel that that ruminating causes you to worry, '
                             'which only worsens the rumination, select these factors.'),
        'video_link_block_04': 'https://www.youtube.com/embed/hwisVnJ0y88?si=OpCWAMaDwTThocO6',
        'placeholder_dd_04': "Select the factor you think is the most influential",
        'finish_01': "You've completed PsySys.",
        'finish_02': 'Explore your Mental-Health-Map!',
        'feedback_text': ("Congratulations! You've completed PsySys and built your personalised mental-health-map. "
                          "You can now load your map into the Edit tab and further tweak it to create the best "
                          "representation of your mental health. Ask yourself:"),
        'feedback_question_01': "Are there personal factors or relations missing?",
        'feedback_question_02': "Are some of the relationships stronger than others?",
        'feedback_question_03': "Is my most influential factor really that central in my map?",
        'feedback_question_04': "Which could be promising treatment targets in my map?",
        'placeholder_enter_factor': "Enter factor",
        'placeholder_enter_connection': "Enter connection",
        'placeholder_color_scheme': "Select color scheme",
        'color_modal_title': "Color Scheme Info",
        'color_modal_default': "",
        'placeholder_sizing_scheme': "Select sizing scheme",
        'sizing_modal_title': "Sizing Scheme Information", 
        'sizing_modal_default': "",
        'inspect_modal_title': "Inspection Mode",
        'inspect_modal_text': ("Within this mode you can further inspect the consequences of a given factor. "
                               "Just click on a factor to see its direct effects."),
        'factor_edit_title': "Factor Info",
        'factor_edit_name': "Name:",
        'factor_edit_severity': "Severity Score:",
        'note': "Note:",
        'save_changes': "Save",
        'connection_edit_title': "Connection Info",
        'connection_edit_strength': "Strength of the connection:",
        'connection_types': "Type:",
        'type_01': "Amplifier",
        'type_02': "Reliever",
        'text_edge_01': "The factor",
        'text_edge_02': "influences the factor",
        'donation_title': "Data Donation",
        'donation_info': ("Here you can anonymously donate your map. Our aim is to continuously improve PsySys to "
                          "provide scientifically backed content for our users. Therefore, it is imporant to analyze "
                          "PsySys results to better understand its clinical value and potential use. By choosing to "
                          "donate your map, you agree that your anonymized data can be used for research purposes."),
        'donation_button': "Yes, I want to donate",
        'plot_modal_title': "Figure Info",
        'psysys_mission': ("PsySys aims to convey the concepts of the network approach to psychopathology directly to "
                           "users. Thereby, it provides users with a framework to better understand their mental health. "
                           "Starting as a Research Master Thesis, the PsySys Project is currently being funded by the "
                           "University of Amsterdam through an Impact Grant."),
        'freelance': 'Freelance Researcher',
        'role_01': "Developer & Project Lead",
        'role_02': "Supervisor", 
        'role_03': "Scientific Advisor",
        'role_04': "Clinical Advisor"
    },
    'de': {
        'welcome_01': "Wilkommen bei PsySys",
        'welcome_02': "Erkunde Deine mentale Gesundheit!",
        'video_link_intro': "https://www.youtube.com/embed/d8ZZyuESXcU?si=CYvKNlf17wnzt4iGrel=0&modestbranding=1",
        'title_block_01': "Jedem geht's mal schlecht",
        'description_block_01': "Erkenne Deine persönlichen Faktoren.",
        'title_block_02': "Die Zusammenhänge erkennen",
        'description_block_02': "Lerne wie Deine Faktoren sich gegenseitig beeinflussen.",
        'title_block_03': "Teufelskreise",
        'description_block_03': "Verstehe, wie man in Abwärtsspiralen stecken bleibt.",
        'title_block_04': "Aus dem Kreislauf ausbrechen",
        'description_block_04': "Finde Ansätze für positive Veränderungen.",
        'video_link_block_01': 'https://www.youtube.com/embed/ttLzT4U2F2I?si=xv1ETjdc1uGROZTo',
        'placeholder_dd_01': "Wähle Deine persönlichen Faktoren aus",
        'video_link_block_02': 'https://www.youtube.com/embed/stqJRtjIPrI?si=1MI5daW_ldY3aQz3',
        'placeholder_dd_02': "Wähle die Faktoren, die miteinander zusammenhängen",
        'example_block_02': ("Beispiel: Wenn Du merkst, dass Sorgen dich unkonzentriert machen, "
                             "wähle diese Faktoren in dieser Reihenfolge aus."),
        'video_link_block_03': 'https://www.youtube.com/embed/EdwiSp3BdKk?si=TcqeWxAlGl-_NUfx',
        'placeholder_dd_03': "Wähle die Faktoren, die sich gegenseitig verstärken",
        'example_block_03': ("Beispiel: Wenn Du merkst, dass Grübeln Sorgen auslöst und das Grübeln "
                             "dadurch nur noch schlimmer wird, wähle diese Faktoren aus."),
        'video_link_block_04': 'https://www.youtube.com/embed/hwisVnJ0y88?si=OpCWAMaDwTThocO6',
        'placeholder_dd_04': "Wähle den Faktor mit dem größten Einfluss.",
        'finish_01': "Du hast PsySys abgeschlossen.",
        'finish_02': "Erkunde Deine Mental-Health-Map!",
        'feedback_text': ("Glückwunsch! Du hast PsySys abgeschlossen und Deine persönliche Mental-Health-Map "
                          "erstellt. Du kannst diese in die „Bearbeiten“-Ansicht laden und weiter anpassen, "
                          "um die beste Darstellung Deiner Psyche zu erstellen. Frag Dich selbst:"),
        'feedback_question_01': "Fehlen einige Faktoren oder Verbindungen?",
        'feedback_question_02': "Sind manche Verbindungen stärker als andere?",
        'feedback_question_03': "Ist der wichtigste Faktor wirklich der zentralste?",
        'feedback_question_04': "Wo in meiner Map könnte ich intervenieren?",
        'placeholder_enter_factor': "Faktor eingeben",
        'placeholder_enter_connection': "Verbindung wählen",
        'placeholder_color_scheme': "Farbschema auswählen",
        'color_modal_title': "Farbschema Info",
        'color_modal_default': "",
        'placeholder_sizing_scheme': "Größenschema auswählen",
        'sizing_modal_title': "Größenschema Info", 
        'sizing_modal_default': "",
        'inspect_modal_title': "Inspektionsmodus",
        'inspect_modal_text': ("In diesem Modus kannst du die Auswirkungen eines bestimmten Faktors genauer "
                               "untersuchen. Klicke einfach auf einen Faktor, um seine direkten Auswirkungen "
                               " zu sehen."),
        'factor_edit_title': "Faktor Info",
        'factor_edit_name': "Name:",
        'factor_edit_severity': "Schweregrad:",
        'note': "Notiz:",
        'save_changes': "Speichern",
        'connection_edit_title': "Verbindung Info",
        'connection_edit_strength': "Stärke der Verbindung:",
        'connection_types': "Typ:",
        'type_01': "Verstärker",
        'type_02': "Dämpfer",
        'text_edge_01': "Der Faktor",
        'text_edge_02': "beeinflusst den Faktor",
        'donation_title': "Daten-Spende",
        'donation_info': ("Hier kannst Du anonym deine Mental-Health-Map an unsere Forschungsgruppe weitergeben. Unser Ziel ist "
                          "es, PsySys kontinuierlich zu verbessern, um wissenschaftlich fundierte Inhalte für unsere Nutzer "
                          "bereitzustellen. Daher ist es wichtig, die PsySys-Ergebnisse zu analysieren, um den klinischen "
                          "Wert und die potenzielle Nutzung besser zu verstehen. Indem Du dich entscheidest deine Map zu "
                          "spenden, stimmst Du zu, dass Die anonymisierten Daten für Forschungszwecke verwendet werden können."),
        'donation_button': "Ja, ich will spenden",
        'plot_modal_title': "Grafik Info",
        'psysys_mission': ("PsySys zielt darauf ab, die Konzepte des Netzwerkansatzes der Psychopathologie direkt an "
                           "Nutzer zu vermitteln. Auf diese Weise bietet es den Nutzern einen Rahmen, um ihre psychische "
                           "Gesundheit besser zu verstehen. Das PsySys-Projekt begann als Masterarbeit und "
                           "wird derzeit von der Universität Amsterdam durch einen Impact Grant gefördert."),
        'freelance': 'Freiberufliche Forscherin',
        'role_01': "Entwicklung & Projektleitung",
        'role_02': "Betreuung", 
        'role_03': "Beratung",
        'role_04': "Beratung"
    }
}