Поиск максимальной клики с помощью CPLEX и применением branch and cut

### easy
| Название           | Время(сек) | Размер клики | Клика                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------|------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-fat200-1.clq     | 0.39598    | 12           | 1,2,38,39,75,76,112,113,149,150,186,187                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| c-fat200-2.clq     | 0.53952    | 24           | 1,2,19,20,37,38,55,56,73,74,91,92,109,110,127,128,145,146,163,164,181,182,199,200                                                                                                                                                                                                                                                                                                                                                                                                          |
| c-fat200-5.clq     | 8.91799    | 58           | 1,2,8,9,15,16,22,23,29,30,36,37,43,44,50,51,57,58,64,65,71,72,78,79,85,86,92,93,99,100,106,107,113,114,120,121,127,128,134,135,141,142,148,149,155,156,162,163,169,170,176,177,183,184,190,191,197,198                                                                                                                                                                                                                                                                                     |
| c-fat500-1.clq     | 1.76163    | 14           | 1,2,81,82,161,162,241,242,321,322,401,402,481,482                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| c-fat500-10.clq    | 31.86377   | 126          | 1,2,9,10,17,18,25,26,33,34,41,42,49,50,57,58,65,66,73,74,81,82,89,90,97,98,105,106,113,114,121,122,129,130,137,138,145,146,153,154,161,162,169,170,177,178,185,186,193,194,201,202,209,210,217,218,225,226,233,234,241,242,249,250,257,258,265,266,273,274,281,282,289,290,297,298,305,306,313,314,321,322,329,330,337,338,345,346,353,354,361,362,369,370,377,378,385,386,393,394,401,402,409,410,417,418,425,426,433,434,441,442,449,450,457,458,465,466,473,474,481,482,489,490,497,498 |
| c-fat500-2.clq     | 2.88084    | 26           | 1,2,41,42,81,82,121,122,161,162,201,202,241,242,281,282,321,322,361,362,401,402,441,442,481,482                                                                                                                                                                                                                                                                                                                                                                                            |
| c-fat500-5.clq     | 10.28604   | 64           | 1,2,17,18,33,34,49,50,65,66,81,82,97,98,113,114,129,130,145,146,161,162,177,178,193,194,209,210,225,226,241,242,257,258,273,274,289,290,305,306,321,322,337,338,353,354,369,370,385,386,401,402,417,418,433,434,449,450,465,466,481,482,497,498                                                                                                                                                                                                                                            |
| gen200_p0.9_55.clq | 305.21397  | 55           | 5,6,12,14,15,19,21,25,26,27,30,33,35,36,41,62,64,67,69,73,76,77,78,79,81,82,86,88,89,91,93,96,107,111,113,116,117,123,129,137,143,144,146,147,159,163,164,175,177,182,187,192,197,198,199                                                                                                                                                                                                                                                                                                  |
| johnson8-2-4.clq   | 0.28708    | 4            | 1,6,15,28                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| johnson8-4-4.clq   | 0.25382    | 14           | 2,7,15,19,23,27,33,38,44,48,52,56,64,69                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| johnson16-2-4.clq  | 13.53179   | 8            | 1,6,15,28,45,66,104,119                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| hamming6-2.clq     | 0.27095    | 32           | 1,4,6,7,10,11,13,16,18,19,21,24,25,28,30,31,34,35,37,40,41,44,46,47,49,52,54,55,58,59,61,64                                                                                                                                                                                                                                                                                                                                                                                                |
| hamming6-4.clq     | 1.12559    | 4            | 1,16,52,61                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| hamming8-2.clq     | 15.00167   | 128          | 1,4,6,7,10,11,13,16,18,19,21,24,25,28,30,31,34,35,37,40,41,44,46,47,49,52,54,55,58,59,61,64,66,67,69,72,73,76,78,79,81,84,86,87,90,91,93,96,97,100,102,103,106,107,109,112,114,115,117,120,121,124,126,127,130,131,133,136,137,140,142,143,145,148,150,151,154,155,157,160,161,164,166,167,170,171,173,176,178,179,181,184,185,188,190,191,193,196,198,199,202,203,205,208,210,211,213,216,217,220,222,223,226,227,229,232,233,236,238,239,241,244,246,247,250,251,253,256                 |
| hamming8-4.clq     | 31.65949   | 16           | 6,11,55,58,84,93,97,112,145,160,164,173,199,202,246,251                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| MANN_a9.clq        | 0.24554    | 16           | 1,6,8,9,11,13,16,20,23,27,28,31,34,37,40,43                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| san200_0.7_1.clq   | 15.25385   | 30           | 2,12,16,19,31,47,49,57,72,81,98,101,111,123,131,136,138,141,142,150,152,157,160,161,163,171,172,175,176,196                                                                                                                                                                                                                                                                                                                                                                                |
| san200_0.9_1.clq   | 4.84916    | 70           | 1,2,5,7,8,11,15,16,21,22,23,24,26,27,32,33,38,39,40,43,48,53,54,56,60,61,62,68,69,71,77,80,92,93,94,104,108,109,110,119,120,121,125,136,142,146,147,151,155,158,159,160,162,163,164,165,167,170,171,172,173,176,183,186,187,189,193,195,198,200                                                                                                                                                                                                                                            |
| san200_0.9_2.clq   | 3.77182    | 60           | 4,10,12,15,17,19,23,24,26,30,33,37,38,46,51,52,56,57,58,59,73,74,75,76,79,83,86,88,92,94,98,99,105,112,114,129,131,133,135,136,138,141,144,149,159,160,161,163,165,167,168,169,170,174,177,179,182,186,195,196                                                                                                                                                                                                                                                                             |

### hard
| Название           | Время(сек) | Размер клики | Клика                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------|------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| brock200_1.clq     | 7200.01333 | 21           | 4,26,32,41,46,48,83,100,103,104,107,120,122,132,137,138,144,175,180,191,199                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| brock200_2.clq     | 1461.92355 | 12           | 27,48,55,70,105,120,121,135,145,149,158,183                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| brock200_3.clq     | 7200.00157 | 15           | 12,29,36,38,58,84,97,98,104,118,130,144,158,173,178                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| brock200_4.clq     | 6507.11308 | 17           | 12,19,28,29,38,54,65,71,79,93,117,127,139,161,165,186,192                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C125.9.clq         | 1560.23209 | 34           | 5,9,11,14,19,25,29,31,34,40,44,45,49,50,52,54,55,66,67,68,70,77,80,96,98,99,103,104,110,114,117,121,122,125                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| gen200_p0.9_44.clq | 7200.00469 | **41(44)**   | 29,30,31,34,38,40,46,58,65,67,72,74,81,82,84,93,97,98,99,100,102,107,108,117,119,120,127,132,138,141,149,150,151,156,170,173,180,186,190,193,197                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| keller4.clq        | 3069.58692 | 11           | 8,12,28,33,43,75,84,111,117,125,149                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| MANN_a27.clq       | 1581.20057 | 126          | 1,2,7,9,15,19,22,24,27,30,33,35,38,42,44,47,51,53,56,60,62,66,67,72,74,76,80,82,85,89,92,94,97,101,104,106,110,114,115,120,123,125,129,130,133,137,139,143,146,150,152,156,158,160,164,167,169,174,175,179,183,185,188,191,193,198,200,204,206,209,211,214,217,222,224,227,229,234,236,239,242,245,247,252,254,256,259,262,267,270,271,276,277,282,283,288,290,293,296,299,301,306,308,310,314,317,320,324,326,328,333,336,337,341,344,346,351,353,356,359,361,365,367,372,373,377                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| MANN_a45.clq       | 7200.08753 | **344(345)** | 1,5,19,21,25,27,29,30,31,33,36,38,39,44,48,51,54,56,59,61,65,67,70,74,76,80,82,86,90,91,94,99,100,105,108,109,112,117,120,123,124,128,132,135,137,139,142,145,150,151,156,157,161,163,167,169,172,176,178,182,184,189,191,193,196,200,202,205,209,212,214,217,221,223,226,230,232,236,238,241,244,247,251,253,257,261,263,266,270,271,276,278,281,285,288,291,294,296,300,301,306,309,311,315,317,319,324,326,330,333,335,338,342,344,348,349,354,355,360,361,364,368,371,373,376,380,382,386,390,391,394,399,401,405,408,411,412,415,420,422,426,427,432,435,438,439,442,446,449,453,455,457,461,465,468,469,473,477,478,481,485,489,490,495,496,499,503,505,508,513,514,517,520,523,528,529,532,535,539,543,544,547,550,555,557,559,563,565,570,572,576,578,581,583,587,590,592,596,598,601,604,609,610,613,616,619,623,625,630,631,634,638,640,643,646,649,652,655,658,661,664,668,670,673,676,681,683,685,690,693,694,697,701,703,706,709,712,715,720,721,724,727,730,733,736,739,742,745,748,751,756,757,762,765,766,771,772,777,778,782,784,788,790,794,796,799,802,805,809,811,815,819,820,823,827,829,832,835,838,841,845,847,852,854,857,859,863,865,869,872,875,877,880,885,886,889,893,896,898,903,904,909,911,913,916,919,922,925,928,931,935,939,940,943,946,949,952,955,960,961,965,967,971,973,976,980,982,986,988,992,994,997,1000,1004,1006,1010,1012,1016,1020,1021,1026,1028,1030,1033 |
| p_hat300-1.clq     | 506.54792  | 8            | 18,49,107,149,171,197,225,255                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| p_hat300-2.clq     | 7200.01087 | 25           | 4,21,30,38,40,44,48,49,56,75,76,139,149,153,159,174,190,199,205,252,255,259,273,290,296                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| p_hat300-3.clq     | 7200.02057 | 36           | 4,19,20,21,24,33,40,49,56,75,76,89,98,139,149,160,166,174,176,190,199,205,219,221,226,235,239,245,247,252,255,273,290,297,298,299                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| san200_0.9_3.clq   | 7200.00654 | **40(44)**   | 8,9,14,18,20,26,27,34,37,40,44,47,50,57,60,74,80,87,89,100,101,111,113,117,119,120,126,131,132,142,143,147,148,159,177,188,189,195,197                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| sanr200_0.7.clq    | 7200.01084 | **17(18)**   | 8,34,35,39,41,42,55,96,105,107,110,124,158,162,176,184,187                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| san200_0.7_2.clq   | 3198.4348  | 18           | 4,6,13,15,23,26,37,51,68,70,111,117,162,164,179,180,192,199                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### other
| Название        | Время(сек) | Размер клики | Клика                                                                                                                                  |
|-----------------|------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------|
| san1000.clq     | 7200.14519 | **10(15)**   | 5,75,76,114,225,368,469,496,716,759                                                                                                    |
| keller4.clq     | 3653.58528 | 11           | 19,24,36,37,71,87,109,111,135,138,163                                                                                                  |
| sanr200_0.9.clq | 7200.00994 | **38(42)**   | 31,47,51,57,60,69,70,72,74,75,78,80,81,85,86,93,94,101,102,118,123,130,135,136,140,143,144,150,153,158,160,164,171,174,175,189,197,198 |
| p_hat1000-1.clq | 1741.1006  | 10           | 9,80,85,226,461,617,623,640,731,785                                                                                                    |
| p_hat1500-1.clq | 7200.45286 | **9(12)**    | 154,497,597,775,968,1212,1292,1399,1475                                                                                                |