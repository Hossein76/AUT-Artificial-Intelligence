x=[35.900000000000794 , 35.900000000000794 , 35.900000000000794 ; ...
30.3334328358209 , 99.89004975124435 , 60.66570480928711 ; ...
6.642885572139429 , 104.08388059701483 , 40.882567164179214 ; ...
1.5642786069650865 , 105.53980099502438 , 31.229481165600564 ; ...
0.6701492537313437 , 117.77044776119352 , 32.036362631288 ; ...
0.3817910447761232 , 121.87502487562143 , 29.67799185888742 ; ...
0.2598009950248779 , 129.09273631840716 , 30.731465748182178 ; ...
0.2101492537313449 , 136.38228855721226 , 31.977724709784315 ; ...
0.18646766169154408 , 139.01114427860614 , 30.72999122036879 ; ...
0.18766169154229015 , 143.62716417910363 , 31.378811207122215 ; ...
0.1336318407960209 , 145.57014925373002 , 30.366344468135598 ; ...
0.14358208955223994 , 151.51223880596962 , 31.157983993078066 ; ...
0.10318407960199077 , 152.72756218905286 , 31.443856716417887 ; ...
0.10895522388059799 , 155.38039800994906 , 30.925144647134733 ; ...
0.1270646766169166 , 159.08577114427666 , 31.38934294047006 ; ...
0.08358208955223935 , 157.5445771144257 , 30.346332851869537 ; ...
0.07522388059701533 , 163.0107462686558 , 31.24856927483799 ; ...
0.05402985074626893 , 164.72457711442635 , 31.512469083155693 ; ...
0.04318407960199019 , 164.82487562189016 , 30.83553045582898 ; ...
0.05621890547263713 , 167.07383084577017 , 31.214190585534013 ; ...
0.04616915422885584 , 167.63482587064547 , 30.746431258342216 ; ...
0.052537313432836144 , 170.28348258706342 , 31.27472174013641 ; ...
0.03263681592039804 , 172.3840796019896 , 31.304404643449452 ; ...
0.04238805970149264 , 172.4563184079586 , 30.928218482057733 ; ...
0.040099502487562354 , 175.1563184079595 , 31.334793380038754 ; ...
0.050945273631841065 , 175.1959203980088 , 30.948005072675937 ; ...
0.036119402985074746 , 176.18905472636794 , 30.957035576832915 ; ...
0.03402985074626875 , 178.3875621890539 , 31.319061058344584 ; ...
0.02049751243781092 , 178.0238805970132 , 30.924116260801394 ; ...
0.02895522388059706 , 180.37820895522356 , 31.318667678556263 ; ...
0.027164179104477687 , 180.17791044776087 , 30.83721882391329 ; ...
0.022686567164179085 , 180.75333333333242 , 31.09348337676686 ; ...
0.02875621890547269 , 184.0979104477617 , 31.399265212399555 ; ...
0.017412935323383068 , 182.73333333333332 , 30.961000965322636 ; ...
0.016119402985074596 , 185.31034825870708 , 31.29919821183944 ; ...
0.02378109452736317 , 185.38467661691513 , 30.936417910447716 ; ...
0.0169154228855721 , 185.28527363184136 , 31.07420023171812 ; ...
0.020796019900497488 , 187.77850746268683 , 31.36476019900479 ; ...
0.02407960199004976 , 187.48656716417761 , 31.112990889707177 ; ...
0.01880597014925368 , 188.77721393034818 , 31.32504943636254 ; ...
0.02159203980099499 , 188.0439800995017 , 30.936948590381434 ; ...
0.016517412935323356 , 190.85283582089554 , 31.192254390697112 ; ...
0.019800995024875576 , 189.61263681592075 , 31.186101258413814 ; ...
0.01582089552238802 , 190.53343283582214 , 31.186904557671536 ; ...
0.018507462686567125 , 192.58805970149248 , 31.265516239029576 ; ...
0.012338308457711427 , 192.76457711442782 , 31.023207041714453 ; ...
0.0161194029850746 , 192.17990049751242 , 31.08918846627082 ; ...
0.01800995024875618 , 194.29601990049832 , 31.37995496203203 ; ...
0.010447761194029839 , 194.15671641791084 , 31.114837154433943 ...
];

y=[0.01 ; ...
0.03 ; ...
0.05 ; ...
0.07 ; ...
0.09 ; ...
0.11 ; ...
0.13 ; ...
0.15 ; ...
0.17 ; ...
0.19 ; ...
0.21 ; ...
0.23 ; ...
0.25 ; ...
0.27 ; ...
0.29 ; ...
0.31 ; ...
0.33 ; ...
0.35 ; ...
0.37 ; ...
0.39 ; ...
0.41 ; ...
0.43 ; ...
0.45 ; ...
0.47 ; ...
0.49 ; ...
0.51 ; ...
0.53 ; ...
0.55 ; ...
0.57 ; ...
0.59 ; ...
0.61 ; ...
0.63 ; ...
0.65 ; ...
0.67 ; ...
0.69 ; ...
0.71 ; ...
0.73 ; ...
0.75 ; ...
0.77 ; ...
0.79 ; ...
0.81 ; ...
0.83 ; ...
0.85 ; ...
0.87 ; ...
0.89 ; ...
0.91 ; ...
0.93 ; ...
0.95 ; ...
0.97  ...
];
y=y*100;
plot(y,x(:,1),'b--o',y,x(:,2),'r-x',y,x(:,3),'g:d');

