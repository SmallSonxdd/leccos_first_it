#order of suites: swords, wands, pentacles, cups; order of ranks: page, knight, queen, king

list_of_cultures = ["Piir-Bakka", "Nat-Bakka", "Au'Pitchai", "Ou'Rangi", #air: avianfolk, batfolk, monkeyfolk, apefolk
"Goritaur", "Daiodi", "Kotharakai", "Quagga", #fire: yetifolk, hogfolk, hyenafolk, zebrafolk
"Blijani", "Vousai", "Panterexi", "Eluabu", #earth: chameleonfolk, gourdfolk, pantherfolk, elephantfolk
"Lutrani", "Arachi", "Kalameghi", "Karchari"] #water: otterfolk, spiderfolk, merfolk, amphibianfolk

dictionary_of_lists_cultures_to_positive_attributes = {
    "Piir-Bakka": "curious, witty, chatty, communicative, inspired, vigilant, alert, mental agility".split(', '), #swords
    "Nat-Bakka": "assertive, direct, impatient, intellectual, daring, focused, perfectionist, ambitious".split(', '),
    "Au'Pitchai": "honest, independent, principled, fair, constructive criticism, objective, perceptive".split(', '),
    "Ou'Rangi": "reason, authority, discipline, integrity, morality, serious, high standards, strict".split(', '),
    "Goritaur": "adventure, excitement, fresh ideas, cheerfulness, energetic, fearless, extroverted".split(', '), #wands
    "Daiodi": "courageous, energetic, charming, hero, rebellious, hot tempered, free spirit".split(', '),
    "Kotharakai": "confident, self-assured, passionate, determined, social, charismatic, vivacious, optimistic".split(', '),
    "Quagga": "leadership, vision, big picture, taking control, daring decisions, boldness, optimism".split(', '),
    "Blijani": "ambitious, diligent, goal oriented, planner, consistent, star student, studious, grounded, loyal, faithful, dependable".split(', '), #pentacles
    "Vousai": "practical, reliable, efficient, stoic, slow and steady, hard-working, committed, patient, conservative".split(', '),
    "Panterexi": "generous, caring, nurturing, homebody, good business sense, practical, comforting, welcoming, sensible, luxurious".split(', '),
    "Eluabu": "abundance, prosperity, security, ambitious, safe, kind, patriarchal, protective, businessman, provider, sensual, reliable".split(', '),
    "Lutrani": "idealism, sensitivity, dreamer, naivete, innocence, inner child, head in the clouds".split(', '), #cups
    "Arachi": "idealist, charming, artistic, graceful, tactful, diplomatic, mediator, negotiator".split(', '),
    "Kalameghi": "compassion, warmth, kindness, intuition, healer, counsellor, supportive".split(', '),
    "Karchari": "wise, diplomatic, balance between head and heart, devoted, advisor, counsellor".split(', '),
}

dictionary_of_lists_cultures_to_negative_attributes = {
    "Piir-Bakka": "scatterbrained, cynical, sarcastic, gossipy, insulting, rude, lack of planning".split(', '), #swords
    "Nat-Bakka": "rude, tactless, forceful, bully, aggressive, vicious, ruthless, arrogant".split(', '),
    "Au'Pitchai": "pessimistic, malicious, manipulative, harsh, bitter, spiteful, cruel, deceitful, unforgiving".split(', '),
    "Ou'Rangi": "irrational, dictator, oppressive, inhumane, controlling, cold, ruthless, dishonest".split(', '),
    "Goritaur": "hasty, impatient, lacking ideas, tantrums, laziness, boring, unreliable, distracted".split(', '), #wands
    "Daiodi": "arrogant, reckless, impatient, lack of self control, passive, volatile, domineering".split(', '),
    "Kotharakai": "demanding, vengeful, low confidence, jealous, selfish, temperamental, bully".split(', '),
    "Quagga": "forceful, domineering, tyrant, vicious, powerless, ineffective, weak leader".split(', '),
    "Blijani": "foolish, immature, irresponsible, lazy, underachiever, procrastinator, missed chances, poor prospects".split(', '), #pentacles
    "Vousai": "workaholic, laziness, dull, boring, no initiative, cheap, irresponsible, gambler, risky investments".split(', '),
    "Panterexi": "selfish, unkempt, jealous, insecure, greedy, materialistic, gold digger, intolerant, self-absorbed, envious".split(', '),
    "Eluabu": "greed, materialistic, wasteful, chauvanist, poor financial decisions, gambler, exploitative, possessive".split(', '),
    "Lutrani": "emotional vulnerability, immaturity, neglecting inner child, escapism, insecurity".split(', '), #cups
    "Arachi": "disappointment, tantrums, moodiness, turmoil, avoiding conflict, vanity".split(', '),
    "Kalameghi": "insecurity, giving too much, overly-sensitive, needy, fragile, dependence, martyrdom".split(', '),
    "Karchari": "overwhelmed, anxious, cold, repressed, withdrawn, manipulative, selfish".split(', '),
}

list_of_open_world = ['wind1', 'wind2', 'wind3', 'wind4', 'wind5', 'sky6', 'sky7', 'sky8', 'sky9', 'sky10', #air
'fire1', 'fire2', 'fire3', 'fire4', 'fire5', 'lightning6', 'lightning7', 'lightning8', 'lightning9', 'lightning10', #fire
'earth1', 'earth2', 'earth3', 'earth4', 'earth5', 'mountain6', 'mountain7', 'mountain8', 'mountain9', 'mountain10', #earth
'water1', 'water2', 'water3', 'water4', 'water5', 'lake6', 'lake7', 'lake8', 'lake9', 'lake10'] #water

dictionary_of_lists_open_world_to_positive_attributes = {
    'wind1': "clarity, breakthrough, new idea, concentration, vision, force, focus, truth".split(', '), #air
    'wind2': "stalemate, difficult choices, stuck in the middle, denial, hidden information".split(', '),
    'wind3': "heartbreak, separation, sadness, grief, sorrow, upset, loss, trauma, tears".split(', '),
    'wind4': "rest, relaxation, peace, sanctuary, recuperation, self-protection, rejuvenation".split(', '),
    'wind5': "arguments, disputes, aggression, bullying, intimidation, conflict, hostility, stress".split(', '),
    'sky6': "moving on, departure, leaving behind, distance, accepting lessons".split(', '),
    'sky7': "lies, trickery, scheming, strategy, resourcefulness,sneakiness, cunning".split(', '),
    'sky8': "trapped, restricted, victimised, paralysed, helpless, powerless, imprisonment".split(', '),
    'sky9': "fear, anxiety, negativity, breaking point, despair, nightmares, isolation".split(', '),
    'sky10': "ruin, failure, bitterness, collapse, exhaustion, dead end, victimization, betrayal".split(', '),
    'fire1': "inspiration, creative spark, new initiative, new passion, enthusiasm, energy".split(', '), #fire
    'fire2': "planning, first steps, making decisions, leaving comfort, taking risks".split(', '),
    'fire3': "momentum, confidence, expansion, growth, foresight, looking ahead".split(', '),
    'fire4': "community, home, celebrations, reunions, parties, gatherings, stability, belonging".split(', '),
    'fire5': "conflict, competition, arguments, aggression, tension, rivals, clashes of ego".split(', '),
    'lightning6': "success, victory, triumph, rewards, recognition, praise, acclaim, pride".split(', '),
    'lightning7': "protectiveness, standing up for yourself, defending yourself, protecting territory".split(', '),
    'lightning8': "movement, speed, progress, quick decisions, sudden changes, excitement".split(', '),
    'lightning9': "last stand, persistence, grit, resilience, perseverance, close to success, fatigue".split(', '),
    'lightning10': "burden, responsibility, duty, stress, obligation, burning out, struggles".split(', '),
    'earth1': "new opportunities, resources, abundance, prosperity, security, stability, manifestation".split(', '), #earth
    'earth2': "balancing resources, adaptation, resourcefulness, flexibility, stretching resources".split(', '),
    'earth3': "teamwork, shared goals, collaboration, apprenticeship, effort, pooling energy".split(', '),
    'earth4': "possessiveness, insecurity, hoarding, stinginess, stability, security, savings, materialism, wealth, frugality, boundaries, guardedness".split(', '),
    'earth5': "hardship, loss, isolation, feeling abandoned, adversity, struggle, unemployment, alienation, disgrace".split(', '),
    'mountain6': "generosity, charity, community, material help, support, sharing, giving and receiving, gratitude".split(', '),
    'mountain7': "harvest, rewards, results, growth, progress, perseverance, patience, planning".split(', '),
    'mountain8': "skill, talent, craftsmanship, quality, high standards, expertise, mastery, commitment, dedication, accomplishment".split(', '),
    'mountain9': "rewarded efforts, success, achievement, independence, leisure, material security, self-sufficiency".split(', '),
    'mountain10': "legacy, roots, family, ancestry, inheritance, windfall, foundations, privilege, affluence, stability, tradition".split(', '),
    'water1': "love, new feelings, emotional awakening, creativity, spirituality, intuition".split(', '), #water
    'water2': "unity, partnership, attraction, connection, close bonds, joining forces, mutual respect".split(', '),
    'water3': "friendship, community, gatherings, celebrations, group events, social events".split(', '),
    'water4': "apathy, contemplation, feeling disconnected, melancholy, boredom, indifference, discontent".split(', '),
    'water5': "loss, grief, disappointment, sadness, mourning, discontent, feeling let down".split(', '),
    'lake6': "nostalgia, memories, familiarity, healing, comfort, sentimentality, pleasure".split(', '),
    'lake7': "choices, searching for purpose, illusion, fantasy, daydreaming, wishful thinking, indecision".split(', '),
    'lake8': "abandonment, walking away, letting go, searching for truth, leaving behind".split(', '),
    'lake9': "wishes coming true, contentment, satisfaction, success, achievements, recognition, pleasure".split(', '),
    'lake10': "happiness, homecomings, fulfillment, emotional stability, security, domestic harmony".split(', '),    
}

dictionary_of_lists_open_world_to_negative_attributes = {
    'wind1': "confusion, miscommunication, hostility, arguments, destruction, brutality".split(', '), #air
    'wind2': "indecision, hesitancy, anxiety, too much information, no right choice, truth revealed".split(', '),
    'wind3': "healing, forgiveness, recovery, reconciliation, repressing emotions".split(', '),
    'wind4': "recovery, awakening, re-entering world, release from isolation, restlessness, burnout".split(', '),
    'wind5': "reconciliation, resolution, compromise, revenge, regret, remorse, cutting losses".split(', '),
    'sky6': "stuck in past, returning to trouble, running away from problems, trapped".split(', '),
    'sky7': "confession, conscience, regret, maliciousness, truth revealed".split(', '),
    'sky8': "freedom, release, taking control, survivor, facing fears, empowered, surrender".split(', '),
    'sky9': "recovery, learning to cope, facing life, finding help, shame, guilt, mental health issues".split(', '),
    'sky10': "survival, improvement, healing, lessons learned, despair, relapse".split(', '),
    'fire1': "delays, blocks, lack of passion, lack of energy, hesitancy, creative blocks".split(', '), #fire
    'fire2': "bad planning, overanalyzing, not taking action, playing it safe, avoiding risk".split(', '),
    'fire3': "restriction, limitations, lack of progress, obstacles, delays, frustration".split(', '),
    'fire4': "lack of support, instability, feeling unwelcome, transience, lack of roots, home conflict".split(', '),
    'fire5': "end of conflict, cooperation, agreements, truces, harmony, peace, avoiding conflict".split(', '),
    'lightning6': "failure, lack of recognition, no rewards, lack of achievement".split(', '),
    'lightning7': "giving up, admitting defeat, yielding, lack of self belief, surrender".split(', '),
    'lightning8': "waiting, slowness, chaos, delays, losing momentum, hastiness, being unprepared".split(', '),
    'lightning9': "stubbornness, rigidity, defensiveness, refusing compromise, giving up".split(', '),
    'lightning10': "failure to delegate, shouldering too much responsibility, collapse, breakdown".split(', '),
    'earth1': "missed chances, scarcity, deficiency, instability, stinginess, bad investments".split(', '), #earth
    'earth2': "imbalance, unorganized, overwhelmed, messiness, chaos, overextending".split(', '),
    'earth3': "lack of cohesion, lack of teamwork, apathy, poor motivation, conflict, ego, competition".split(', '),
    'earth4': "generosity, giving, spending, openness, financial insecurity, reckless spending".split(', '),
    'earth5': "positive changes, recovery from loss, overcoming adversity, forgiveness, feeling welcomed".split(', '),
    'mountain6': "power dynamics, abuse of generosity, strings attached gifts, inequality, extortion".split(', '),
    'mountain7': "unfinished work, procrastination, low effort, waste, lack of growth, setbacks, impatience, lack of reward".split(', '),
    'mountain8': "lack of quality, rushed job, bad reputation, lack of motivation, mediocrity, laziness, low skill, dead-end job".split(', '),
    'mountain9': "being guarded, living beyond means, material instability, reckless spending, superficiality".split(', '),
    'mountain10': "family disputes, bankruptcy, debt, fleeting success, conflict over money, instability, breaking traditions".split(', '),
    'water1': "coldness, emptiness, emotional loss, blocked creativity, feeling unloved, gloominess".split(', '), #water
    'water2': "separation, rejection, division, imbalance, tension, bad communication, withdrawal".split(', '),
    'water3': "gossip, scandal, excess, isolation, loneliness, solitude, imbalanced social life".split(', '),
    'water4': "clarity, awareness, acceptance, choosing happiness, depression, negativity".split(', '),
    'water5': "acceptance, moving on, finding peace, contentment, seeing positives".split(', '),
    'lake6': "stuck in past, moving forward, leaving home, independence".split(', '),
    'lake7': "lack of purpose, disarray, confusion, diversion, distractions, clarity, making choices".split(', '),
    'lake8': "stagnation, monotony, accepting less, avoidance, fear of change, staying in bad situation".split(', '),
    'lake9': "unhappiness, lack of fulfilment, disappointment, underachievement, arrogance, snobbery".split(', '),
    'lake10': "unhappy home, separation, domestic conflict, disharmony, isolation".split(', '),
}