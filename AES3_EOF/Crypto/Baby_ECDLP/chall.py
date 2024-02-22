from sage.all import *
from Crypto.Util.number import *
from secret import p, q, flag

assert isPrime(p) and isPrime(q)
n = p * q
a, b = matrix(ZZ, [[p, 1], [q, 1]]).solve_right(
    vector([p**2 - p**3, q**2 - q**3])
)
E = EllipticCurve(Zmod(n), [a, b])
G = E(p, p) + E(q, q)
C = bytes_to_long(flag) * G

print(f"{a = }")
print(f"{b = }")
print(f"C =", C.xy())


# a = -154628303413020099603005855302249563989659660175225286251094576128161431662287667599372218889125088137567812189323005126051275141507294672376122081477233859915859727872423263490671340278425685590972818120389616973587947067209132215519650801263171190195093248530680189195973377279272859452392619165927530069
# b = 23076174172014468546239164849045747588555523290787256166772459492700318142569763564777157579738591025503065586936556930247369768234363802437442128472819475851980929483003303653950262141705197061780944333630958551451399418967411855676332865630644847083802410164360804671966986361796789118576230538139167486264530641584939833520435649820652362597137202740207999381837922542566084624691268060489835949323840484982352199086280486979778839176690911725719577536749
# C = (43251707765136040834510703815884581701165733704488490462213976648968018796504026879815230443980943095899827410342713160401456071809110511372964500342826324313715386146999610346038107808796139887658646459851257418230882154250060547935069586951919553123655767565083276270980894015621047334579186972400823276, 14770433932569738040821577251543581880877008780410217700429917131320618722087864792672682625536045422138805174267036688681974566218278172292659595438675976711729754161677018344464703526872893653110858720076157467067870190614090772482725435612438028103885320506078006341162292894050129833825117693251732662)