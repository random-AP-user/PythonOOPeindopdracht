
# Eindopdracht: Stem systeem
    Eindopdracht Python OOP 2024 
    Naam: Noah Verstraeten
    Username: random-AP-user
    StudentID: 152232


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)





![verkiezing](https://assets.vlaanderen.be/image/upload/ar_16:9,c_fill,q_auto:eco,w_500/INTER_VERKIEZING_coverillustratie_folder_d9yyfm)

[Source image](https://www.vlaanderen.be/inter/toolbox-toegankelijke-steden-en-gemeenten/algemeen-bestuur-dienstverlening-en-communicatie/algemeen-bestuur/klantvriendelijk-onthaal-van-personen-met-een-handicap-en-ouderen-op-verkiezingsdag)

## Demo website: 
vooraf gegenereerde uitslag: [PythonOOPeindopdracht](https://random-ap-user.github.io/PythonOOPeindopdracht/website/)


## Extra Functies

- unieke ID voor de kiezers
- schaalbaare lijsten
- responcive website & live update
- encrypte ID voor validatie en anonimiteit

## Documentatie

### 1. ```main.py```

    In dit bestand word alles geactiveerd en doorgegeven. Het haalt alle kiezers uit "./json/voters.json" om dan met dit bestand de rest van de code te kunnen uitvoeren

### 2. ```voters.py```

    voor dat de class "voters" aangemaakt word maakt men een class "voter" voor iedere kiezer daar word de naam, achternaam en leeftijd van de JSON ingestoken met een extra variabel voor hun ID te bepalen.

### 3. ```parties.py```

    Na da alle de class voters is gemaakt gaat men er paar willekeurige mensen er uitkiezen om dan er een kandidaat van te maken. deze kandidaat word dan in hun class "party" gestoken en om alles bij te houden word er een class "parties" gemaakt.

### 4. ```chipcard.py```

    Voor dat de stemming begint instantieer de main één chip kaart voor de kiezer omdat er maar 3 kies computers zijn houd het geen rekening als het boven de 60 chip kaarten zit. deze chip kaart krijgt ook een ID om de identiteit te verbergen van de stemmer. Als oplossing voor het latere kiezer ticket probleem word er een variabel "ballotReciept" aangemaakt waar ik later het ticket aan mee geef. Ook word er een "hasVoted" toegevoegd zodat u niet oneindig veel keren kunt stemmen.

### 5. ```votecomputer.py```

    In de main word er drie kies computers gemaakt. De computers worden eerst opgestart met de "usb.usbCode" deze bevat een code dat overeenkomt met de code in de computer als dat zo is word het systeem opgestart. De kies computer krijg de class "parties" met data van partijen en kandidaten met hun voorgestelde zetel lijst. Deze computer bevat het stem systeem met de class "VoteCompiter" dat checkt op als het aan/uit mag en een printer deze printer geeft de BallodID, het partij dat de kiezer gekozen heeft, mogelijke voorkeur kandidaten en de chipcard ID om later alles te verifiëren. De printer kan meerdere keren printen voor uitzonderingen te voorkomen zoals verlies tijdens transport. Het belangrijke is wel als men meerdere keren wilt stemmen word het oude nog steeds afgedrukt met een melding dat dit niet mag. 

### 6. ```scanner.py```
	
    In de main word er nagekeken als de “reciept” zelfs klopt en niet gefraudeerd is dus men gebruikt de chipID met een secret key om het de juiste reciept ID uit te komen na deze check gaat de luik van de stembus open 


### 7. ```ballotbox.py```

deze stembus programma heeft een class "BallotBox" dat alle geldige stemmen bijhoud en kan weergegeven worden.


### 8. ```getResults.py```

    als iedereen gestemd heeft en de computer 'uitgezet' is kan men alle resultaten opvragen. de manier dat het op gelijst word is door eerst alle stemmen op partijen op te vragen ze worden met elks opgeteld en daarna gesorteerd op hoeveel het partij voorkwam in de lijst (x: x[1]). er word voor elk partij een kandidaat lijst bij gemaakt die op de zelfde manier werkt zoals bij de partijen maar in de plaats sorteer ik het bij  kandidaat zijn "rank" (x[0].rank). voor de kandidaten word er de totale stemmen en originele ranklijst bijgehouden omdat het interessant is om te vergelijken in de toekomst. alles word dan samen genomen in een JSON genaamd "output.txt" dat kan gebruikt worden om op andere plaatsen de score te kunnen laten weergeven.


### 9. ```website/...```
    hier word er de verkiezing uitgave gevisualiseerd zodat het makelijker is om deze data te kunnen bekijken. deze data word uit de "output.json" bestand genomen door fetch zodat men de pagina niet elke keer vanaf 0 moet opbouwen.


## Uitwerking

Om de verkiezing simulatie te starten:

```Bash
  py ./main.py
```

Octivate an mython server to bypass CORS
```Bash
  python -m http.server
```


## Author



- [@Noah Verstraeten](https://github.com/random-AP-user)


