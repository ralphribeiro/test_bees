def before_scenario(context, scenario):
    if 'skip' in scenario.effective_tags:
        scenario.skip(reason="skip")