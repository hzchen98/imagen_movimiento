import talkey
tts = talkey.Talkey(
    
    espeak = {
        'languages': {
            'es': {
                'voice': 'spanish-mb-es1',
                'words_per_minute': 130
            },
        }
    })
tts.say('christopher caraculo, lalalalalala!')
