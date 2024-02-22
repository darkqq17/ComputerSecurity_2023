from sage.all import *
from Crypto.Util.number import *

# 在SageMath环境中运行

var('p q')
a = -154628303413020099603005855302249563989659660175225286251094576128161431662287667599372218889125088137567812189323005126051275141507294672376122081477233859915859727872423263490671340278425685590972818120389616973587947067209132215519650801263171190195093248530680189195973377279272859452392619165927530069
b = 23076174172014468546239164849045747588555523290787256166772459492700318142569763564777157579738591025503065586936556930247369768234363802437442128472819475851980929483003303653950262141705197061780944333630958551451399418967411855676332865630644847083802410164360804671966986361796789118576230538139167486264530641584939833520435649820652362597137202740207999381837922542566084624691268060489835949323840484982352199086280486979778839176690911725719577536749
C = (43251707765136040834510703815884581701165733704488490462213976648968018796504026879815230443980943095899827410342713160401456071809110511372964500342826324313715386146999610346038107808796139887658646459851257418230882154250060547935069586951919553123655767565083276270980894015621047334579186972400823276, 14770433932569738040821577251543581880877008780410217700429917131320618722087864792672682625536045422138805174267036688681974566218278172292659595438675976711729754161677018344464703526872893653110858720076157467067870190614090772482725435612438028103885320506078006341162292894050129833825117693251732662)
Cx = 43251707765136040834510703815884581701165733704488490462213976648968018796504026879815230443980943095899827410342713160401456071809110511372964500342826324313715386146999610346038107808796139887658646459851257418230882154250060547935069586951919553123655767565083276270980894015621047334579186972400823276
Cy = 14770433932569738040821577251543581880877008780410217700429917131320618722087864792672682625536045422138805174267036688681974566218278172292659595438675976711729754161677018344464703526872893653110858720076157467067870190614090772482725435612438028103885320506078006341162292894050129833825117693251732662
# Cx = C[0]
# Cy = C[1]

# 定义方程
eq1 = p*a + b == p**2 - p**3
eq2 = q*a + b == q**2 - q**3
# 解方程
solutions = solve([eq1, eq2], p, q)

# 打印可能的解
for sol in solutions:
    print(f"Possible solution: {sol}")

#從上面可能的解中，選出唯一兩組可能的(p, q > 0, p != q)，結果就是(p = 77.....,q = 12...) pr (p = 12...., q = 77....), 這邊選用哪一個不影響

p = 248614771719323216082473810405221350280953187468072198589547109245203456057395347877116585934513393025407032409940023141369967473362638543702586904312411
q = 204738697349410648958147607342886806249982347231437960650735436645770485808646943469245406723978236797887477089357052170860651513523936228914042180759467
n = p * q
E = EllipticCurve(Zmod(n), [a, b])
G = E(p, p) + E(q, q)  # 根据您之前的描述构建G


# Define the curves and points modulo p and q
E_p = EllipticCurve(Zmod(p), [a, b])   #curve
E_q = EllipticCurve(Zmod(q), [a, b])   #curve

c = E(Cx, Cy)
cp = E_p(Cx, Cy)
cq = E_q(Cx, Cy)

G_p = E_p(p, p) + E_p(q,q)   #point
G_q = E_q(p, p) + E_q(q,q)  #point

order_p = G_p.order()
order_q = G_q.order()

print(order_p)
print(order_q)


d_p = discrete_log(cp, G_p, operation = '+')
d_q = discrete_log(cq, G_q, operation = '+')

crt_flag = crt([d_p, d_q], [order_p, order_q])

# 轉換回字串形式的flag
flag = long_to_bytes(crt_flag)
print('flag = ', flag)