
#include <stdio.h>
#include <stdlib.h>

long sub_CE5(long long *a1)
{
  int i; // [rsp+8h] [rbp-10h]
  int j; // [rsp+Ch] [rbp-Ch]
  int v4; // [rsp+10h] [rbp-8h]

  for ( i = 0; i <= 2; ++i )
  {
    for ( j = 0; j <= 2; ++j )
    {
      v4 = a1[3 * i + j];
      if ( j || v4 <= 0 )
      {
        if ( j && v4 < 0 )
          a1[3 * i + j] = -a1[3 * i + j];
      }
      else
      {
        a1[3 * i] = -a1[3 * i];
      }
    }
  }
  return 0;
}

long sub_C22(long long *a1)
{
  int i; // [rsp+8h] [rbp-10h]
  int j; // [rsp+Ch] [rbp-Ch]

  for ( i = 0; i <= 2; ++i )
  {
    for ( j = 0; j <= 2; ++j )
    {
      if ( a1[3 * i + j] < 0 )
        a1[3 * i + j] = -a1[3 * i + j];
    }
  }
  return 0;
}

long sub_AFB(long long *a1)
{
  int i; // [rsp+8h] [rbp-10h]
  int j; // [rsp+Ch] [rbp-Ch]
  int v4; // [rsp+10h] [rbp-8h]

  for ( i = 0; i <= 2; ++i )
  {
    for ( j = 0; j <= 2; ++j )
    {
      v4 = a1[3 * i + j];
      if ( j == 1 && v4 > 0 )
      {
        a1[3 * i + 1] = -a1[3 * i + j];
      }
      else if ( j != 1 && v4 < 0 )
      {
        a1[3 * i + j] = -a1[3 * i + j];
      }
    }
  }
  return 0;
}

long long sub_9DE(long long *a1, long long *a2)
{
  int i; // [rsp+14h] [rbp-Ch]
  long long v4; // [rsp+18h] [rbp-8h]

  v4 = 0;
  for ( i = 0; i <= 2; ++i )
    v4 += a1[i] * a2[i];
  return v4;
}

long sub_A41(long long *a1, long long *a2)
{
  int i; // [rsp+18h] [rbp-28h]
  int j; // [rsp+1Ch] [rbp-24h]
  long long v5[3]; // [rsp+20h] [rbp-20h]

  for ( i = 0; i <= 2; ++i )
    v5[i] = sub_9DE(a1 + 3 * i, a2);
  for ( j = 0; j <= 2; ++j )
    a2[j] = v5[j];
  return 0;
}

long long tab[100][3] = {{4677356919945, 3064867953928, 5592055376297},
{2998267079000243, 1372573835216724, 3297508818811285},
{2693408991487025, 1276200312094632, 2980459567250257},
{918187912247193, 937126679793824, 1311973877856665},
{37905038896305, 106132886245192, 112698631386833},
{671540010385799, 814001534661600, 1055255648637049},
{718622171878105, 172682699819448, 739078575478777},
{1770050542390485, 899585600352868, 1985530955432093},
{860456390100775, 2260864892978112, 2419069090283737},
{268622978427615, 594315835079432, 652203661723457},
{107492549585917, 207496254695556, 233686422218245},
{10011216032237, 4588087680084, 11012492678965},
{69236729437153, 77463803026104, 103895935832065},
{76148596018118455, 76413077227836888, 107877555807303913},
{19153010682199, 11101927582200, 22137990293449},
{1083818658441863, 1812642186497016, 2111950420974745},
{821727124567233, 825626018221456, 1164857840774465},
{732909608059, 4606883593500, 4664818639309},
{122049673426737, 199318857397816, 233718055994705},
{334946656468579, 911832142890900, 971404714569829},
{1257534099376269, 1257989993708260, 1778744173669781},
{217201450289135, 131567972947848, 253942122369073},
{211221612670767, 97221236478344, 232522124714225},
{1727226450211069, 2005747521775260, 2646948116494981},
{1739896476581711, 1773475047030000, 2484442289862961},
{2340962747829, 481438629140, 2389956012221},
{1839356500718445, 1230981548128148, 2213266343793077},
{7746579837089301, 7593194164200500, 10847400462214301},
{49737180768175, 56019538192968, 74913121748593},
{3055068869802165, 3099736906732732, 4352219513098493},
{2277367765499245, 2066432016281052, 3075149625180277},
{1487867674469717, 1360050662883444, 2015809520351965},
{1998510678421025, 1299119676217152, 2383643611133473},
{1392472904820459, 2500846843809260, 2862379382061341},
{9012806969469, 19410309124220, 21400719374981},
{296726776434885, 263251811869852, 396671521924877},
{1355585155230639, 600080127262480, 1482466617572561},
{6074377725501, 27692333938780, 28350721749701},
{21661361298815, 6894684459168, 22732163273857},
{51985509899229, 43827592347340, 67995228438821},
{59216409086395, 50090745816132, 77560724090893},
{4396011560067083, 2122521661176156, 4881599721239485},
{43758748848521, 40943880066720, 59926867227529},
{287238942997451, 163743539149740, 330632964157501},
{475352604278505, 779538553550288, 913039131070313},
{431743342201367, 159539478403656, 460277262858505},
{1119902707158185, 1083143395977048, 1558005677059273},
{113588200772629, 132623012210460, 174617131812829},
{216044421482549, 130424835611100, 252360515528701},
{905927611893811, 1562548905772740, 1806173834635861},
{468914535581947, 513926696708196, 695702157010765},
{2002193483005995, 4362369796555988, 4799900934946013},
{4858694145113751, 9696492354729880, 10845684523399049},
{390278217489621, 106611495198620, 404577678518429},
{14891950277883419, 9004296160296660, 17402515117685869},
{1438328947011145, 714561110038512, 1606047240833737},
{11416203809007, 7451377311976, 13632781567025},
{39761745874945733, 13024866036238644, 41840692755805645},
{3430396151152837, 1750546079125284, 3851237376348685},
{2835099813005459, 6261292068482220, 6873250273090741},
{1445584196339679, 1488152265363320, 2074683309233729},
{4364512016845737, 2071934837641816, 4831343407027145},
{3555897450796449, 2125587976740560, 4142768509999649},
{133830193237235, 75877079270148, 153843595188373},
{42206735708147, 75488437050204, 86486488351765},
{1581082998372327, 4274369405693536, 4557417828559385},
{113430162573435, 68511972507812, 132515252549837},
{126080249265627, 63433990652164, 141138585882605},
{256263027837879, 275948747857280, 376587905913929},
{2676210314828985, 2908704120403448, 3952551240559577},
{200210450605395, 77621044251932, 214730647655093},
{605464435612085, 1208244320880948, 1351459034426173},
{5728837703963, 17538888302316, 18450804435565},
{3088458530640665, 6411485397031032, 7116580716315193},
{5843429711336475, 5910413677421932, 8311357327752557},
{668805703452987, 404622420205316, 781677920824205},
{1454731728095, 791185572672, 1655964676897},
{5710811349049, 5637632047320, 8024728117849},
{181125834306945, 204747111677752, 273364130042273},
{425620451556371, 506389629639300, 661500737557621},
{62599036502947, 67274866352604, 91894216433125},
{11020547702616507, 4105123272597724, 11760293735654285},
{102619959517623, 202454312509064, 226977101807465},
{194633565418845, 178786222397948, 264285334642277},
{5456887482145, 2014037418672, 5816697320353},
{141874663488471, 590172315009200, 606985816591529},
{1624374668077567, 3409406956446144, 3776592228048385},
{116331132901315, 126126821439972, 171583529421253},
{12055031267065, 19964320397088, 23321618034937},
{505955286491817, 519235067629256, 724979866882505},
{745118201767491, 1498952833093660, 1673935700809541},
{3551030402718035, 5859952245604548, 6851923616167477},
{74459185872669, 35494820143660, 82486681457381},
{518526760917965, 842041635498828, 988890346652053},
{1099223298700175, 2950603127673672, 3148706191031953},
{60269245771175, 56157321722112, 82377343783513},
{998464845980885, 888643016899092, 1336644477841117},
{1736206973494197, 769381662740404, 1899042600304445},
{444500394749031, 502848618244600, 671146283460281},
{1558625382945999, 689634541679720, 1704379325573201}};



int main(void){
    long long v6[3],i, v5;
    long long v9[9], x, A;
    x = 0;
    A = 0;
    while (1)
    {

        L:
        v6[0] = 3;
        v6[1] = 4;
        v6[2] = 5;

        v9[0] = 1;
        v9[1] = 2;
        v9[2] = 2;
        v9[3] = 2;
        v9[4] = 1;
        v9[5] = 2;
        v9[6] = 2;
        v9[7] = 2;
        v9[8] = 3;
        srand(x);
        for(i = 0;i<25;i++)
        {
            v5 = rand() % 3;
            if ( v5 )
            {
                if ( v5 == 1 )
                    sub_C22(v9);
                else
                    sub_CE5(v9);
            }
            else
            {
                sub_AFB(v9);
            }
            sub_A41(v9, v6);
            if(A)
            {
                printf("[0x%lx, 0x%lx, 0x%lx],\n", v6[0], v6[1], v6[2]);
            }
        }
        if(A)
          return 0;
        for(i=0;i<100;i++)
        {
            if(tab[i][0] == v6[0])
            {
                if(tab[i][1] == v6[1])
                    if(tab[i][2] == v6[2])
                    {
                        printf("%lld %lld %lld\n",tab[i][0],tab[i][1],tab[i][2]);
                        printf("%lld\n",x);
                        A = 1;
                        goto L;
                    }
            }
        }
        x += 1;
    }
    return 0;
}
