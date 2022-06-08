import numpy as np
from scipy.signal import savgol_filter
from kneed import KneeLocator
import matplotlib.pyplot as plt


ignore_n =0
y = [0.29532715678215027, 0.040607329457998276, 0.0160214863717556, 0.009136045351624489, 0.03611156716942787, 0.0013611558824777603, 0.00028610581648536026, 0.001532446127384901, 6.130311521701515e-05, 0.001419414533302188, 0.001294346759095788, 0.0013680366100743413, 0.0013141501694917679, 0.00106907170265913, 0.0011727320961654186, 0.0030955402180552483, 0.0013101787772029638, 0.0012339698150753975, 0.0012814321089535952, 0.00023270369274541736, 0.0012689965078607202, 6.761496479157358e-05, 0.00012632893049158156, 0.001366141834296286, 0.00032984628342092037, 0.00010625208233250305, 0.0012951524695381522, 0.0002348023554077372, 0.00014362981892190874, 0.0002815042098518461, 0.0012845085002481937, 0.002023227047175169, 7.568966248072684e-05, 7.568966248072684e-05, 6.142729398561642e-05, 0.0022086731623858213, 0.00014270833344198763, 0.0001080086876754649, 0.00023809584672562778, 0.00020592717919498682, 0.0002352134615648538, 8.149795030476525e-05, 0.001196022960357368, 0.001210849266499281, 0.00018246614490635693, 0.00018246614490635693, 0.00018246614490635693, 0.0011167589109390974, 0.00018620881019160151, 0.0014495090581476688, 0.001970642013475299, 0.000295401579933241, 0.00011621311568887904, 5.5002732551656663e-05, 8.005707059055567e-05, 0.00021571473916992545, 0.0366019606590271, 0.09258227795362473, 0.004939315840601921, 0.006137722171843052, 0.003141217865049839, 0.0011779565829783678, 0.0052538178861141205, 0.00043781817657873034, 0.0003723404952324927, 3.5456741898087785e-05, 0.00048642916954122484, 0.00023637828417122364, 0.00043781817657873034, 0.0004841392219532281, 0.00041473680175840855, 0.0003021383017767221, 0.0011102965800091624, 9.252471500076354e-05, 5.289390901452862e-05, 0.0006347268936224282, 0.000655433745123446, 0.000655433745123446, 3.277168798376806e-05, 0.005200656596571207, 0.0024391754996031523, 0.00030762481037527323, 0.0002399477525614202, 0.0002399477525614202, 0.0003586580860428512, 0.0004012013669125736, 0.00023638387210667133, 0.004939315840601921, 0.004939316306263208, 0.0007660735864192247, 0.004939316306263208, 0.0049597653560340405, 6.852115620858967e-05, 8.821934170555323e-05, 0.03623608127236366, 0.002766136545687914, 0.0001316272682743147, 5.933868305874057e-05, 5.933868305874057e-05, 5.933868305874057e-05, 9.879059507511556e-05, 0.002177347894757986, 0.0008939302060753107, 0.0006092916009947658, 0.0018884814344346523, 0.002059739548712969, 0.00024234165903180838, 0.00041845679515972733, 0.00024234165903180838, 0.0021510047372430563, 0.0001542978861834854, 0.0001542978861834854, 0.0034699859097599983, 0.0013038311153650284, 0.00024600536562502384, 0.001916795503348112, 0.0001168058006442152, 8.799957140581682e-05, 0.00017390563152730465, 0.00014025757263880223, 0.00014025757263880223, 0.0019412189722061157, 0.002364795422181487, 7.89272235124372e-05, 7.89272235124372e-05, 0.002432587556540966, 0.00010990593727910891, 0.00010990593727910891, 0.00015112066466826946, 0.00010990593727910891, 0.002775692380964756, 0.0003497446596156806, 4.2771396692842245e-05, 0.006552800070494413, 0.00041104413685388863, 0.003174492157995701, 0.0008911752374842763, 0.0005765195819549263, 0.0005014175549149513, 0.000560037384275347, 0.00031868729274719954, 0.002650843933224678, 0.00016564715770073235, 0.0002638643200043589, 0.00021572911646217108, 0.03673149645328522, 0.010101629421114922, 0.00013565766857936978, 0.0001595592184457928, 0.00013565766857936978, 0.00013565766857936978, 0.0001898002956295386, 0.00013565766857936978, 0.00013565766857936978, 0.0002653763222042471, 0.00013565766857936978, 0.00013565766857936978, 0.00013565766857936978, 0.00013565766857936978, 0.00016109348507598042, 0.0006022193119861186, 0.00010534184548305348, 0.00015959155280143023, 0.00013565766857936978, 0.00022218015510588884, 0.00013565766857936978, 0.00015600632468704134, 0.0001755071134539321, 0.0003487538197077811, 0.00025130980066023767, 0.0003283795085735619, 0.00013565766857936978, 0.00021590432152152061, 0.00015982169134076685, 0.00036584914778359234, 0.00013565766857936978, 0.00013565766857936978, 0.00013565766857936978, 0.00015461677685379982, 0.00015461677685379982, 0.00017370896239299327, 7.690620259381831e-05, 0.00019119602802675217, 0.00038438296178355813, 0.033873625099658966, 0.005224893335253, 0.0012696125777438283, 0.0010907065588980913, 0.00019462693308014423, 0.0007600018288940191, 0.005609437357634306, 0.0007422432536259294, 0.0007085203542374074, 0.00024351415049750358, 0.000525884737726301, 0.0004563838301692158, 0.0013720991555601358, 0.004462497774511576, 0.00043818383710458875, 8.715756121091545e-05, 0.0009670573053881526, 3.022054079337977e-05, 0.00017942782142199576, 0.00020497027435339987, 0.005893101915717125, 0.00022099132183939219, 0.00020078648230992258, 0.00018037486006505787, 0.00018037486006505787, 0.00022099132183939219, 0.00036641478072851896, 5.496221638168208e-05, 0.00020079971000086516, 0.00020079971000086516, 0.00020079971000086516, 0.00020079971000086516, 0.00020079971000086516, 0.00020079971000086516, 0.000535567058250308, 0.0003778494137804955, 0.00028789881616830826, 0.0003400422865524888, 0.0001282325538340956, 0.00029225408798083663, 0.0005359578644856811, 0.0003282545949332416, 0.00035711139207705855, 0.0001636059896554798, 3.9675393054494634e-05, 3.9675393054494634e-05, 8.988480840343982e-05, 3.9675393054494634e-05, 4.1045452235266566e-05, 4.1045452235266566e-05]    



# x = range(0, len(y))
x = np.arange(len(y) - ignore_n)

print('x: ', len(x))
y = np.array(y)
idx_y = np.argsort(y)[::-1]

y = y[idx_y]

print('y: ' ,len(y))

y = y[ignore_n:]
print('new y: ' ,len(y))

half_length = int(len(y)/2)
if half_length % 2 == 0:
    window = half_length + 1
else:
    window = half_length

smoothed_y = savgol_filter(y, window, 1)

sensitivity = 1


kn = KneeLocator(x, y, curve='convex', direction='decreasing', S=sensitivity)
print('kn: ', kn.knee)

kn_smooth = KneeLocator(x, smoothed_y, curve='convex', direction='decreasing', S=sensitivity)
print('smoothed kn: ', kn_smooth.knee)



plt.xlabel('k')
plt.ylabel('PageRank values')
plt.plot(x, y, 'bx-')
plt.plot(x, smoothed_y, 'rx-')

plt.vlines(kn.knee, plt.ylim()[0], plt.ylim()[1], linestyles='dashed')
plt.vlines(kn_smooth.knee, plt.ylim()[0], plt.ylim()[1], linestyles='dotted')

plt.show()
