from dash import html

# Initialize factor list
factors = ["Loss of interest", "Sadness", "Loss of motivation", "Stress", "Worry", "Overthinking",
           "Sleep problems", "Tiredness", "Physical pain", "Changes in appetite", "Self-blame",
           "Concentration problems", "Procrastination", "Guilt", "Shame", "Hopelessness", "Interpersonal problems",
           "Social isolation", "Irritability", "Anxiety", "Reduced activity", "Self-neglect", "Suicidal thoughts", 
           "Fear of the future", "Substance abuse"]

# Initialize node color schemes
node_color = ["Uniform", "Severity", "Severity (abs)", "Out-degree", "In-degree", "Out-/In-degree ratio"]

# Initialize node sizing schemes
node_size = ["Uniform", "Severity", "Severity (abs)", "Out-degree", "In-degree", "Out-/In-degree ratio"] 

# Stylesheet
stylesheet = [{'selector': 'node',
               'style': {'background-color': '#9CD3E1', 
                         'label': 'data(label)', 
                         'font-family': 'Arial'}},
              {'selector': 'edge',
               'style': {'curve-style': 'bezier', 
                         'target-arrow-shape': 'triangle', 
                         'control-point-step-size': '40px' }}
    ]

# Initialize styles (buttons)
hidden_style = {'display': 'none'}
visible_style = {'display': 'block', "color": "#8793c9"}

# Dictionary
translations = {
    'en': {
        'factors': ["Loss of interest", "Sadness", "Loss of motivation", "Stress", "Worry", "Overthinking", 
                    "Sleep problems", "Tiredness","Physical pain", "Changes in appetite", "Self-blame", 
                    "Concentration problems", "Procrastination", "Guilt", "Shame", "Hopelessness", "Interpersonal problems",
                    "Social isolation", "Irritability", "Anxiety", "Reduced activity", "Self-neglect", "Suicidal thoughts", 
                    "Fear of the future", "Substance abuse"],
        'welcome_01': 'Welcome to PsySys',
        'welcome_02': 'Dive into your mental health!',
        'suicide-prevention': html.P(["If you're experiencing ",
                                      html.Span("suicidal thoughts", style={"fontWeight": "bold"}),
                                      ", support is available. Please reach out to ",
                                      "someone you trust or contact a confidential suicide prevention hotline. ",
                                      "You can find a hotline near you by visiting ",
                                      html.A("this link", href="https://findahelpline.com", 
                                             target="_blank", 
                                             style={"color": "blue", 
                                                    "textDecoration": "underline"}),
                                    ". Remember, you're not alone."]), 
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
        'edit-map-title_01': "Edit your map",
        'edit-map-title_02': "Load, customize & save maps",
        'compare-map-title_01': "Compare your map",
        'compare-map-title_02': "Upload maps & track changes",
        'placeholder_enter_factor': "Enter factor to add/delete",
        'placeholder_enter_connection': "Enter connection to add/delete",
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
        'role_04': "Clinical Advisor",
        'plot_01': "Influence Plot",
        'plot_01_title': "Factor Influence",
        'plot_01_y': "Connections",
        'plot_01_out': "Out-going",
        'plot_01_in': "In-coming",
        'plot_02': "Severity Tracker",
        'plot_02_title': "Severity Comparison",
        'plot_02_y': "Severity",
        'plot_01_modal': ("The figure shows the number of in-coming and out-going links for each factor in the map. "
                          "Factors with many out-going links have a lot of influence on the map. Factors with many "
                          "in-coming links are strongly influenced by the other factors in the map."),
        'plot_02_modal': "The figure shows the factor severity scores over the uploaded mental-health maps.",
        'no_note_message': "No note available.",
        'modal_color_default': "As a default the factors in your map are uniformly colored.",
        'modal_color_uniform': "All the factors in your map have the same color.",
        'modal_color_severity': ("The factors in your map are colored based on their relative severity. The darkest factor "
                                 "has the highest indicated severity and the lightest factor has lowest indicated severity."),
        'modal_color_severity_abs': ("The factors in your map are colored based on their absolute severity. The darkest "
                                     "factor has the highest possible severity score (10) and the lightest factor has the "
                                     "lowest possible severity score (0)"),
        'modal_color_out': ("The factors in your map are colored based on their out-degree, which refers to the number of "
                            "out-going connections. The darkest factor has the most out-going connections and the lightest "
                            "factor has the least out-going connections. Factors with a lot of out-going connections can be "
                            "seen as main causes in your map."),
        'modal_color_in': ("The factors in your map are colored based on their in-degree, which refers to the number of "
                           "incoming connections. The darkest factor has the most incoming connections and the lightest "
                           "factor has the least incoming connections. Factors with a lot of incoming connections can be "
                           "seen as main effects in your map."),
        'modal_color_out-in': ("The factors in your map are colored based on their out-/in-degree ratio, which is "
                               "calculated by dividing the number of out-going by the number of incoming connections. "
                               "The darkest factor has many out-going and few incoming connections (active), and the "
                               "lightest factor has few out-going and many incoming connections (passive)."),
        'modal_size_default': ("As a default the size of the factors in your map corresponds to their relative severity. "
                               "The largest factor has the highest indicated severity and the smallest factor has lowest "
                               "indicated severity."),
        'modal_size_uniform': "All factors in your map have the same size.",
        'modal_size_severity': ("The size of the factors in your map corresponds to their relative severity. The largest "
                                "factor has the highest indicated severity and the smallest factor has lowest indicated "
                                "severity."),
        'modal_size_severity_abs': ("The size of the factors in your map corresponds to their absolute severity. The "
                                    "largest factor has the highest possible severity score (10) and the smallest factor "
                                    "has the lowest possible severity score (0)."),
        'modal_size_out': ("The size of the factors in your map corresponds to their out-degree, which refers to the number "
                           "of out-going connections. The largest factor has the most out-going connections and the smallest "
                           "factor has the least out-going connections. Factors with a lot of out-going connections can be "
                           "seen as main causes in your map."),
        'modal_size_in': ("The size of the factors in your map corresponds to their in-degree, which refers to the number "
                          "of incoming connections. The largest factor has the most incoming connections and the smallest "
                          "factor has the least incoming connections. Factors with a lot of incoming connections can be "
                          "seen as main effects in your map."),
        'modal_size_out-in': ("The size of the factors in your map corresponds to their out-/in-degree ratio, which is "
                               "calculated by dividing the number of out-going by the number of incoming connections. "
                               "The largest factor has many out-going and few incoming connections (active), and the "
                               "smallest factor has few out-going and many incoming connections (passive)."),
        'hover-load-psysys': "Load PsySys map to customize",
        'hover-upload-map': "Upload saved map to edit (.json file)",
        'hover-download-map': "Download map to save & edit later",
        'hover-save-image': "Download image of map",
        'hover-donate': "Donate map to research",
        'hover-back-edit': "Undo last change",
        'hover-uniform': "same color, severity determines factor size",
        'hover-upload-tracking': "Upload saved map to compare (.json file)",
        'hover-delete-tracking': "Delete current map (you can't delete PsySys map)",
        'schemes': ["Uniform", "Severity", "Severity (abs)", "Out-degree", "In-degree", "Out-/In-degree ratio"]
    },
    'de': {
        'factors': ["Interessenverlust", "Traurigkeit", "Motivationsverlust", "Stress", "Sorgen", "Überdenken", 
                    "Schlafstörungen", "Müdigkeit", "Schmerzen", "Veränderter Appetit", "Selbstvorwürfe", 
                    "Konzentrationsprobleme", "Verlangsamtes Denken", "Gedächtnisprobleme", "Prokrastination", 
                    "Schuldgefühle", "Schamgefühle", "Hoffnungslosigkeit", "Beziehungsprobleme", "Soziale Isolation", 
                    "Reizbarkeit", "Ängstlichkeit", "Verminderte Aktivität", "Selbstvernachlässigung", "Suizidgedanken", 
                    "Zukunftsangst", "Substanzmissbrauch"],
        'welcome_01': "Wilkommen bei PsySys",
        'welcome_02': "Erkunde Deine mentale Gesundheit!",
        'suicide-prevention': html.P(["Wenn Du ", 
                                      html.Span("suizidale Gedanken", style={"fontWeight": "bold"}), 
                                      " hast, ist Unterstützung verfügbar. Bitte wende Dich an eine vertraute Person, ",
                                      "oder kontaktiere eine Suizidpräventionshotline. ",
                                      "Du kannst eine Hotline in Deiner Nähe finden, indem Du ",
                                      html.A("diesen Link", href="https://findahelpline.com", target="_blank", 
                                             style={"color": "blue", "textDecoration": "underline"}),
                                             " besuchst. Denke daran, Du bist nicht allein."]),
        'video_link_intro': "https://www.youtube.com/embed/iAD3SAvDc2s?si=ZE9nz2ghhzqtwuTZ",
        'title_block_01': "Jedem geht's mal schlecht",
        'description_block_01': "Erkenne Deine persönlichen Faktoren.",
        'title_block_02': "Die Zusammenhänge erkennen",
        'description_block_02': "Lerne wie Deine Faktoren sich gegenseitig beeinflussen.",
        'title_block_03': "Teufelskreise",
        'description_block_03': "Verstehe, wie man in Abwärtsspiralen stecken bleibt.",
        'title_block_04': "Aus dem Kreislauf ausbrechen",
        'description_block_04': "Finde Ansätze für positive Veränderungen.",
        'video_link_block_01': "https://www.youtube.com/embed/VbtrHB-R8aQ?si=SLZj1ykaXey-shvZ",
        'placeholder_dd_01': "Wähle Deine persönlichen Faktoren aus",
        'video_link_block_02': "https://www.youtube.com/embed/p3iVzuhIhrk?si=0YsKJkr-HgVDVJkN",
        'placeholder_dd_02': "Wähle die Faktoren, die miteinander zusammenhängen",
        'example_block_02': ("Beispiel: Wenn Du merkst, dass Sorgen dich unkonzentriert machen, "
                             "wähle diese Faktoren in dieser Reihenfolge aus."),
        'video_link_block_03': "https://www.youtube.com/embed/98JNUCJrbbA?si=Eci1YF2-pd4iZDZx",
        'placeholder_dd_03': "Wähle die Faktoren, die sich gegenseitig verstärken",
        'example_block_03': ("Beispiel: Wenn Du merkst, dass Grübeln Sorgen auslöst und das Grübeln "
                             "dadurch nur noch schlimmer wird, wähle diese Faktoren aus."),
        'video_link_block_04': "https://www.youtube.com/embed/gUMGu49w7o0?si=sUabGZ5BheGLgA_F",
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
        'edit-map-title_01': "Bearbeite Deine Map",
        'edit-map-title_02': "Uploade, individualisiere & speicher Maps",
        'compare-map-title_01': "Vergleiche Deine Map",
        'compare-map-title_02': "Uploade Maps & tracke Veränderungen",
        'placeholder_enter_factor': "Faktor zum hinzufügen/löschen",
        'placeholder_enter_connection': "Verbindung zum hinzufügen/löschen",
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
        'role_04': "Beratung",
        'plot_01': "Einfluss",
        'plot_01_title': "Faktor Einfluss",
        'plot_01_y': "Verbindungen",
        'plot_01_out': "Ausgehend",
        'plot_01_in': "Eingehend",
        'plot_02': "Schweregrad",
        'plot_02_title': "Faktor Schweregrad Vergleich",
        'plot_02_y': "Schweregrad",
        'plot_01_modal': ("Die Abbildung zeigt die Anzahl der eingehenden und ausgehenden Verbindungen für jeden Faktor "
                          "in der Mental-Health-Map. Faktoren mit vielen ausgehenden Verbindungen haben einen großen Einfluss "
                          "auf die Map. Faktoren mit vielen eingehenden Verbindungen werden stark von den anderen Faktoren "
                          "in der Map beeinflusst."),
        'plot_02_modal': "Die Abbildung vergleicht den Schweregrad der Faktoren über alle hochgeladenen Mental-Health-Maps.",
        'no_note_message': "Keine Notiz verfügbar.",
        'modal_color_default': "Standardmäßig sind die Faktoren in der Map einheitlich gefärbt.",
        'modal_color_uniform': "Alle Faktoren in der Map haben die gleiche Farbe.",
        'modal_color_severity': ("Die Faktoren in der Map sind nach ihrem relativen Schweregrad eingefärbt. Der dunkelste "
                                 "Faktor hat den höchsten Schweregrad und der hellste Faktor den niedrigsten Schweregrad."),
        'modal_color_severity_abs': ("Die Faktoren in der Map sind nach ihrem absoluten Schweregrad eingefärbt. "
                                     "Der dunkelste Faktor hat den höchstmöglichen Schweregrad (10) und der hellste "
                                     "Faktor hat den niedrigsten Schweregrad (0)"),
        'modal_color_out': ("Die Faktoren in der Map sind nach ihrer 'out-degree Zentralität' eingefärbt, welche sich aus "
                            "der Anzahl der ausgehenden Verbindungen ergibt. Der dunkelste Faktor hat die meisten "
                            "ausgehenden Verbindungen und der hellste Faktor hat die wenigsten ausgehenden Verbindungen. "
                            "Faktoren mit vielen ausgehenden Verbindungen können als Hauptursachen in der Map gesehen werden."),
        'modal_color_in': ("Die Faktoren in der Map sind nach ihrer 'in-degree Zentralität' eingefärbt, welche sich aus"
                           "der Anzahl der eingehenden Verbindungen ergibt. Der dunkelste Faktor hat die meisten eingehenden "
                           "Verbindungen und der hellste Faktor hat die wenigsten eingehenden Verbindungen. Faktoren mit "
                           "vielen eingehenden Verbindungen können als Haupteffekte in der Map gesehen werden."),
        'modal_color_out-in': ("Die Faktoren in der Map sind nach dem Verhältnis zwischen ausgehenden und eingehenden "
                               "Verbindungen gefärbt, das berechnet wird, indem die Anzahl der ausgehenden durch die Anzahl "
                               "der eingehenden Verbindungen geteilt wird. Der dunkelste Faktor hat viele ausgehende und "
                               "wenige eingehende Verbindungen (aktiv), und der hellste Faktor hat wenige ausgehende und "
                               "viele eingehende Verbindungen (passiv)."),
        'modal_size_default': ("In der Standardeinstellung entspricht die Größe der Faktoren in der Map ihrem relativen "
                               "Schweregrad. Der größte Faktor hat den höchsten angegebenen Schweregrad und der kleinste "
                               "Faktor hat den niedrigsten Schweregrad."),
        'modal_size_uniform': "Alle Faktoren in der Map haben die gleiche Größe.",
        'modal_size_severity': ("Die Größe der Faktoren in der Map entspricht ihrem relativen Schweregrad. Der größte "
                                "Faktor hat den höchsten angegebenen Schweregrad und der kleinste Faktor den niedrigsten "
                                "angegebenen Schweregrad."),
        'modal_size_severity_abs': ("Die Größe der Faktoren in der Map entspricht ihrem absoluten Schweregrad. Der größte "
                                    "Faktor hat den höchstmöglichen Schweregrad (10) und der kleinste Faktor hat den "
                                    "niedrigsten Schweregrad (0)."),
        'modal_size_out': ("Die Größe der Faktoren in der Map entspricht ihrer 'out-degree Zentralität', die sich aus "
                           "der Anzahl der ausgehenden Verbindungen ergibt. Der größte Faktor hat die meisten ausgehenden "
                           "Verbindungen und der kleinste Faktor hat die wenigsten ausgehenden Verbindungen. Faktoren mit "
                           "vielen ausgehenden Verbindungen können als Hauptursachen in der Map gesehen werden."),
        'modal_size_in': ("Die Größe der Faktoren in der Map entspricht ihrer 'in-degree Zentralität', der sich aus der "
                          "Anzahl der eingehenden Verbindungen ergibt. Der größte Faktor hat die meisten eingehenden "
                          "Verbindungen und der kleinste Faktor hat die wenigsten eingehenden Verbindungen. Faktoren mit "
                          "vielen eingehenden Verbindungen können als Haupteffekte in der Map gesehen werden."),
        'modal_size_out-in': ("Die Größe der Faktoren in der Map entspricht dem Verhältnis zwischen ausgehenden und "
                              "eingehenden Verbindungen, das berechnet wird, indem die Anzahl der ausgehenden durch die "
                              "Anzahl der eingehenden Verbindungen geteilt wird. Der größte Faktor hat viele ausgehende "
                              "und wenige eingehende Verbindungen (eher aktiv), und der kleinste Faktor hat wenige "
                              "ausgehende und viele eingehende Verbindungen (eher passiv)."),
        'hover-load-psysys': "PsySys Map zur Bearbeitung laden",
        'hover-upload-map': "Gespeicherte Map zur Bearbeitung hochladen (.json Datei)",
        'hover-download-map': "Map herunterladen zum speichern & späteren Bearbeiten",
        'hover-save-image': "Bild der Map herunterladen",
        'hover-donate': "Map an Forschung spenden",
        'hover-back-edit': "Letzte Änderung rückgängig machen",
        'hover-uniform': "gleiche Farbe, Schweregrad bestimmt Faktorgröße",
        'hover-upload-tracking': "Gespeicherte Map zum Vergleich hochladen (.json Datei)",
        'hover-delete-tracking': "Map löschen (Du kannst die PsySys Map nicht löschen)",
        'schemes': ["Einheitlich", "Schweregrad", "Schweregrad (abs)", "Out-degree", "In-degree", "Out-/In-degree Verhältnis"]
    }
}
