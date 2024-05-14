"""
Every array lists the floors he visited in that hour.
If he falls a significant part, like more than 2 or 3 obstacles far,
we write down the floor where he landed.
"""
wirtual1 = [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 2, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1]
wirtual2 = [0, 1, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 0, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1]
wirtual3 = [2, 0, 0, 0, 1, 2, 0, 1, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 0, 0, 0, 1, 2, 0, 1, 0, 1, 2]
wirtual4 = [0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 1, 2, 0, 0, 0, 1, 2, 0, 1, 2, 0]
wirtual5 = [1, 2, 1, 2, 1, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 0, 0, 1, 0, 1, 1, 2, 0, 1]
wirtual6 = [2, 0, 1, 2, 0, 1, 0, 1, 2, 1, 2, 3, 0, 1, 2, 0, 1, 2, 3, 0, 0, 1, 2, 0, 1, 2, 0, 1]
wirtual7 = [2, 0, 0, 1, 0, 1, 2, 3, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 0, 0, 1, 2, 3]
wirtual8 = [0, 1, 2, 0, 1, 0, 1, 2, 1, 2, 0, 1, 2, 1, 2, 3, 4, 0, 1, 2, 3, 0, 1, 1, 0, 1, 2, 1, 1, 1]
wirtual9 = [2, 0, 1, 2, 1, 0, 1, 0, 1, 2, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 3, 4, 0]
wirtual10 = [1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 0, 1, 2, 1, 2, 0, 1, 0, 1, 2, 3, 0, 1, 2, 0, 1, 2, 3, 3, 4, 0, 1, 2, 0, 1, 2]
wirtual11 = [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 2, 0, 1, 2, 2, 3, 4, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 0, 1]
wirtual12 = [2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 0, 1, 2, 0, 1, 0, 0, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
wirtual13 = [3, 4, 3, 4, 4, 3, 4, 3, 4, 1, 2, 0, 1, 2, 3, 4, 4, 3, 4, 3, 4, 3, 4, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0]
wirtual14 = [0, 0, 0, 1, 2, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 3, 4, 3, 4, 0, 1, 2, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2]
wirtual15 = [0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 0, 1, 1, 2, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 0, 0, 1, 2, 0, 1, 2, 3, 4]
wirtual16 = [4, 0, 1, 0, 1, 0, 1, 0, 1, 2, 3, 0, 0, 1, 2, 3, 3, 4, 3, 3, 4, 0, 1, 0, 1, 2, 0, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 0, 1, 0, 1]
wirtual17 = [2, 0, 1, 2, 0, 1, 0, 1, 2, 3, 4, 4, 5, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 1, 2, 0]
wirtual18 = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 3, 4, 0, 1, 2, 3, 4, 3, 4, 3, 4, 4, 0, 1, 2, 1, 2, 3, 4, 0, 1, 2, 3, 3, 4]
wirtual19 = [5, 6, 5, 0, 1, 2, 3, 0, 1, 2, 0, 1, 2, 3, 4, 3, 4]
wirtual20 = [0, 1, 2, 1, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 0, 1, 0, 1, 0, 0, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2, 0, 1, 0, 1, 2, 3]
wirtual21 = [4, 2, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 0, 1, 0, 0, 1, 2, 0, 1, 2, 1, 2, 0, 1, 2, 1, 2, 3, 4, 4, 5, 4, 5]
wirtual22 = [6, 0, 1, 2, 0, 1, 2, 0, 0, 1, 2, 3, 4, 5, 5, 0, 1, 2, 3, 2, 3, 4, 4]
wirtual23 = [5, 0, 1, 2, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5, 4, 5, 6, 5]
wirtual24 = [6, 0, 1, 2, 0, 1, 2, 0, 0, 0, 1, 2, 0, 0, 1, 2, 3, 4, 3, 4, 3, 4, 5, 1, 2, 3, 4, 5, 0, 1, 2, 3]
wirtual25 = [4, 5, 5, 6, 5, 6, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]
wirtual26 = [0, 1, 2, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 2, 3, 4, 3, 4, 5, 2, 3, 4, 5, 0, 1, 0, 0, 1, 2, 0, 1, 0, 1]
wirtual27 = [2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 3, 4, 3, 4, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 3, 0, 1, 2, 0, 1, 2, 0, 1]
wirtual28 = [2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 2, 0, 1, 2, 3, 4, 0, 0, 1, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 1, 2, 2, 0, 1, 1]
wirtual29 = [2, 0, 0, 1, 2, 0, 0, 1, 1, 2, 3, 4, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 3, 0, 0, 1, 0, 1, 2, 3, 4, 5, 6, 4, 4, 5, 4, 5, 6, 0, 1, 0]
wirtual30 = [1, 2, 0, 1, 2, 3, 4, 5, 4, 5, 4, 5, 0, 1, 2, 3, 2, 0, 1, 2, 0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 0, 1, 0, 0, 1, 0, 1]
wirtual31 = [2, 0, 1, 2, 3, 4, 0, 1, 2, 1, 2, 3, 4, 3, 4, 1, 2, 0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 4, 5, 5, 6, 6, 3]
wirtual32 = [4, 5, 6, 0, 1, 2, 0, 1, 0, 1, 2, 3, 4, 0, 1, 2, 3, 2, 3, 4, 5, 6, 0, 1, 2, 0, 1, 2, 3, 4, 5]
wirtual33 = [6, 2, 3, 0, 1, 2, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 1, 2, 3, 4, 3, 4, 5, 6, 6, 6, 6, 1, 2, 3, 4, 5, 6]
wirtual34 = [5, 5, 6, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 2, 3, 4, 1, 2, 3, 4, 3, 4, 0]
wirtual35 = [1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 4, 5, 6, 6, 6, 7]
wirtual36 = [3, 4, 3, 4, 0, 1, 0, 1, 0, 1, 2, 3, 4, 5, 2, 3, 4, 5, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5, 5]
wirtual37 = [6, 3, 4, 5, 6, 0, 1, 2, 0, 1, 0, 1, 2, 3, 3, 4, 5, 5, 0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 0, 1, 2, 3, 4]
wirtual38 = [5, 0, 1, 2, 0, 1, 2, 3, 4, 5, 5, 6, 6, 6, 6, 7, 3, 4, 5, 0, 1, 0, 1, 2, 3, 4, 5]
wirtual39 = [6, 0, 1, 2, 0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5, 0, 1, 2, 0, 1, 1, 2, 3, 4, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6]
wirtual40 = [0, 1, 2, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 5, 6, 6, 7, 3, 4, 1, 2, 3, 4, 5, 0, 0, 1, 2, 3, 4]
wirtual41 = [5, 0, 1, 2, 1, 2, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 3, 4, 5, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5]
wirtual42 = [6, 7, 0, 1, 2, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 3, 0, 1, 2, 2, 1, 0, 1, 2, 0, 1, 0, 1, 2, 3, 4, 1, 2, 3, 4]
wirtual43 = [5, 6, 4, 5, 1, 2, 3, 4, 5, 6, 7, 3, 4, 3, 4, 5, 2, 3, 4, 0, 1, 2, 0, 1, 0, 1, 2, 3, 4, 5, 5, 6, 5, 6]
wirtual44 = [7, 6, 1, 2, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 3, 4, 3, 4, 5, 6, 6, 6]
wirtual45 = [6, 7, 6, 7, 3, 4, 5, 6, 5, 6, 7, 0, 1, 2, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 1]
wirtual46 = [2, 0, 1, 2, 2, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 2, 3, 4, 5, 0, 1, 2, 3, 4, 4, 5, 0, 1, 0, 1, 2]
wirtual47 = [0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 5, 5, 6, 0, 1, 0, 1, 0, 1, 2, 3, 4, 5, 1, 2, 0, 1, 2, 3, 4, 5, 6, 0, 1, 1, 2, 3]
wirtual48 = [4, 0, 1, 2, 0, 1, 2, 3, 4, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 0, 1, 0, 1, 0, 1, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3]
wirtual49 = [4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 3, 4, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 0, 1, 2, 1, 2, 3, 4, 5]
wirtual50 = [6, 5, 6, 3, 4, 5, 6, 7, 3, 4, 5, 6, 3, 4, 5, 6, 0, 1, 0, 1, 2, 3, 4, 5, 6, 5, 6, 7]
wirtual51 = [6, 5, 5, 6, 5, 4, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 2, 3, 4, 4, 5, 6, 7, 6, 6, 7, 6, 7, 4, 5, 6]
wirtual52 = [0, 0, 1, 2, 3, 4, 5, 6, 4, 0, 1, 2, 0, 1, 2, 3, 4, 5, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 3, 4, 5, 6, 6, 0, 1, 0, 1, 2]
wirtual53 = [3, 4, 5, 6, 7, 4, 5, 6, 0, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 7, 6, 7, 0, 1, 2, 3, 0, 1, 0, 1]
wirtual54 = [2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 7, 7, 0, 1, 2, 3, 4, 5, 6, 7]
wirtual55 = [0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 0, 1, 2, 0, 1, 2, 3, 4, 5]
wirtual56 = [2, 3, 4, 5, 5, 6, 0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 0, 1, 0, 1, 2]
wirtual57 = [3, 4, 5, 6, 7, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 0, 1, 0, 1, 2, 3, 4, 0, 1, 2, 1, 0, 1, 2]
wirtual58 = [3, 4, 0, 1, 2, 0, 1, 0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 1, 2]
wirtual59 = [0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 3, 4, 5, 6, 6, 0, 1, 0, 1, 0, 1, 2, 3, 4, 5, 0, 1, 2, 0, 1, 2, 3, 3]
wirtual60 = [4, 5, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 5, 6, 6, 7, 0, 1, 2, 3, 0, 1, 2, 0, 1, 0, 1, 1, 2, 0, 1]
wirtual61 = [2, 3, 4, 3, 4, 5, 6, 7, 7, 7, 0, 1, 2, 3, 4, 1, 1, 2, 3, 4, 5, 5, 5, 6, 4, 5, 5, 5, 0, 1, 2]
wirtual62 = [3, 4, 5, 6, 6, 7, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 0, 0, 1, 2, 0, 1, 2, 3]
wirtual63 = [4, 3, 4, 5, 6, 6, 5, 6, 7, 8, 5, 0, 1, 2, 3, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3]
wirtual64 = [4, 3, 4, 0, 1, 2, 3, 4, 5, 6, 7, 6, 7, 8, 4, 5, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 0, 1, 2, 0]
wirtual65 = [1, 2, 3, 4, 5, 6, 6, 7, 6, 0, 1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6]
wirtual66 = [7, 8, 4, 5, 6, 5, 6, 7, 8, 0, 1, 2, 2, 3, 4, 0, 1, 2, 3]
wirtual67 = [4, 4, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 4, 5, 6, 7, 8]
wirtual68 = [9, 9, 0, 1, 2, 3, 1, 2, 3, 4, 5, 6]
wirtual69 = [2, 3, 4, 5, 6, 7, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 1, 2, 3]
wirtual70 = [4, 3, 4, 4, 5, 4, 5, 6, 7, 6, 7, 7, 0, 1, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 0, 1, 2, 3, 4, 4, 0, 1, 0, 1, 2, 3, 4]
wirtual71 = [5, 1, 2, 0, 1, 2, 3, 4, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 5, 6, 5, 6, 0, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8]
wirtual72 = [8, 9, 9, 8, 9, 1, 0, 0, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 3, 0, 1, 2, 0, 1, 2, 3, 4, 5, 0, 1, 2, 0]
wirtual73 = [1, 2, 3, 4, 5, 6, 6, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 6, 7, 8]
wirtual74 = [0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 0, 1, 2, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 5, 6, 3, 4, 0, 1, 2, 3, 4, 1, 0, 1, 0, 1, 2, 0, 1, 2]
wirtual75 = [3, 4, 5, 6, 7, 8, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 7, 6, 7, 6, 7, 8, 9]
wirtual76 = [9, 9, 9, 10, 2, 3, 0, 1, 2, 3, 4, 5]
wirtual77 = [6, 7, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 1, 2, 3, 4, 5, 6, 7, 6, 7, 8]
wirtual78 = [9, 10, 10, 4, 5, 6, 5, 6, 7, 0, 1, 2, 0, 1, 2, 3]
wirtual79 = [4, 5, 6, 0, 1, 0, 1, 2, 3, 4, 3, 4, 5, 5, 6, 3, 4, 3, 4, 5, 0, 1, 0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 0, 1, 0, 1, 2, 3, 4]
wirtual80 = [4, 5, 6, 7, 6, 7, 8, 0, 1, 2, 0, 1, 2, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 3, 4, 5, 0, 1, 2, 0, 1, 2, 3, 4, 5]
wirtual81 = [0, 1, 2, 3, 4, 5, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 6, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
wirtual82 = [7, 3, 0, 1, 2, 0, 1, 2, 3, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 3, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 0, 1, 0, 0, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7]
wirtual83 = [8, 4, 3, 4, 5, 6, 7, 6, 6, 6, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 0, 0, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 3, 4, 4]
wirtual84 = [5, 6, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 6, 7, 0, 0]
wirtual85 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 9, 9, 9, 10, 11]
wirtual86 = [3, 4, 5, 6, 5, 6, 0, 1, 2, 3, 4, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 5]
wirtual87 = [6, 7, 8, 0, 0, 1, 0, 1, 0, 1, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 6, 7, 8, 9, 8]

wirtual = [wirtual1, wirtual2, wirtual3, wirtual4, wirtual5, wirtual6, wirtual7, wirtual8, wirtual9, wirtual10, wirtual11, wirtual12, wirtual13, wirtual14,
           wirtual15, wirtual16, wirtual17, wirtual18, wirtual19, wirtual20, wirtual21, wirtual22, wirtual23, wirtual24, wirtual25, wirtual26, wirtual27,
           wirtual28, wirtual29, wirtual30, wirtual31, wirtual32, wirtual33, wirtual34, wirtual35, wirtual36, wirtual37, wirtual38, wirtual39, wirtual40,
           wirtual41, wirtual42, wirtual43, wirtual44, wirtual45, wirtual46, wirtual47, wirtual48, wirtual49, wirtual50, wirtual51, wirtual52, wirtual53,
           wirtual54, wirtual55, wirtual56, wirtual57, wirtual58, wirtual59, wirtual60, wirtual61, wirtual62, wirtual63, wirtual64, wirtual65, wirtual66,
           wirtual67, wirtual68, wirtual69, wirtual70, wirtual71, wirtual72, wirtual73, wirtual74, wirtual75, wirtual76, wirtual77, wirtual78, wirtual79,
           wirtual80, wirtual81, wirtual82, wirtual83, wirtual84, wirtual85, wirtual86, wirtual87]
