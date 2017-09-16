# Calcola i minuti e i secondi

minute = float(raw_input('Inserisci i minuti >>>'))
hours = minute / 60.0
em = (hours - int(hours)) * 60
es = (em - int(em)) * 60
print minute, ' minuti equivalgono a ', int(hours) , ' ore ', int(em), ' minuti e ', es, ' secondi.'