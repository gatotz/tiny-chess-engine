import json,os,sys,urllib.request as r
from array import array as A
U=os.environ.get("MAKEFUN_ENV_URL")or sys.exit()
N=[0];B=100000;T={};W=[0,100,320,330,500,900,0]
P="@@@@@@@@BEE66EEBB>;@@;>B@@@JJ@@@BBELLEBBEEJOOJEEYYYYYYYY@@@@@@@@',1111,',6@BB@6,1BEGGEB11@GJJG@11BGJJGB11@EGGE@1,6@@@@6,',1111,'6;;;;;;6;B@@@@B;;EEEEEE;;@EEEE@;;BBEEBB;;@BEEB@;;@@@@@@;6;;;;;;6@@@BB@@@>@@@@@@>>@@@@@@>>@@@@@@>>@@@@@@>>@@@@@@>BEEEEEEB@@@@@@@@6;;>>;;6;@B@@@@;;BBBBB@;@@BBBB@>>@BBBB@>;@BBBB@;;@@@@@@;6;;>>;;6JOE@@EOJJJ@@@@JJ;666666;611,,1161,,'',,11,,'',,11,,'',,11,,'',,1"
Q=[ord(c)-64 for c in P]
def H(p,b):
 q=r.Request(U+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"});return json.load(r.urlopen(q))
def S(n):return(ord(n[1])-49)*16+ord(n[0])-97
def Z(q):return"abcdefgh"[q&7]+str((q>>4)+1)
def F(f):
 p=f.split();b=A("b",bytes(128))
 for i,w in enumerate(p[0].split("/")):
  x=0
  for c in w:
   if c.isdigit():x+=int(c)
   else:b[(7-i)*16+x]="PNBRQK".index(c.upper())+1 if c.isupper() else-"PNBRQK".index(c.upper())-1;x+=1
 s=1 if p[1]=="w" else-1;c=0
 if p[2]!="-":
  for k in p[2]:c|={"K":1,"Q":2,"k":4,"q":8}[k]
 return b,s,c,S(p[3])if p[3]!="-"else-1
def D(b,q,y):
 for d in(15,17):
  t=q-d*y
  if not(t&136)and b[t]==y:return 1
 for d in(31,33,14,18,-14,-18,-31,-33):
  t=q+d
  if not(t&136)and b[t]==2*y:return 1
 for d in(15,17,16,1,-1,-16,-15,-17):
  t=q+d
  if not(t&136)and b[t]==6*y:return 1
 for v,ds in((3,(15,17,-15,-17)),(4,(16,1,-1,-16))):
  for d in ds:
   t=q+d
   while not(t&136):
    z=b[t]
    if z:
     if z==v*y or z==5*y:return 1
     break
    t+=d
 return 0
def K(b,s):
 for i in range(128):
  if b[i]==6*s:return i
 return-1
def G(b,s,c,e):
 m=[]
 for f in range(128):
  if f&136:continue
  p=b[f]
  if p*s<=0:continue
  t=abs(p)
  if t==1:
   d=16*s;u=f+d
   if not(u&136)and not b[u]:
    if u>>4 in(0,7):
     for v in(5,4,3,2):m.append(f|(u<<7)|(v<<14))
    else:
     m.append(f|(u<<7));v=f+2*d
     if(f>>4)==(1 if s==1 else 6)and not b[v]:m.append(f|(v<<7))
   for z in(d-1,d+1):
    u=f+z
    if u&136:continue
    if b[u]*s<0:
     if u>>4 in(0,7):
      for v in(5,4,3,2):m.append(f|(u<<7)|(v<<14))
     else:m.append(f|(u<<7))
    elif u==e:m.append(f|(u<<7))
  elif t==2 or t==6:
   for d in((31,33,14,18,-14,-18,-31,-33)if t==2 else(15,17,16,1,-1,-16,-15,-17)):
    u=f+d
    if u&136:continue
    if b[u]*s<=0:m.append(f|(u<<7))
   if t==6:
    if s==1:
     if c&1 and not b[5]and not b[6]and b[7]==4 and not D(b,4,-s)and not D(b,5,-s)and not D(b,6,-s):m.append(f|(6<<7))
     if c&2 and not b[3]and not b[2]and not b[1]and b[0]==4 and not D(b,4,-s)and not D(b,3,-s)and not D(b,2,-s):m.append(f|(2<<7))
    else:
     if c&4 and not b[117]and not b[118]and b[119]==-4 and not D(b,116,-s)and not D(b,117,-s)and not D(b,118,-s):m.append(f|(118<<7))
     if c&8 and not b[115]and not b[114]and not b[113]and b[112]==-4 and not D(b,116,-s)and not D(b,115,-s)and not D(b,114,-s):m.append(f|(114<<7))
  else:
   for d in((15,17,-15,-17)if t==3 else(16,1,-1,-16)if t==4 else(15,17,-15,-17,16,1,-1,-16)):
    u=f+d
    while not(u&136):
     if b[u]==0:m.append(f|(u<<7))
     elif b[u]*s<0:m.append(f|(u<<7));break
     else:break
     u+=d
 return m
def X(b,s,c,e,m):
 f=m&127;t=(m>>7)&127;v=(m>>14)&7;n=b[:];p=n[f];n[f]=0
 if abs(p)==1 and t==e and n[t]==0:n[t-16*s]=0
 n[t]=v*s if v else p
 if abs(p)==6 and abs(t-f)==2:
  k=t&7==6;n[t-1 if k else t+1]=4*s;n[t+1 if k else t-2]=0
 o=c
 if f==4 or t==4:o&=~3
 if f==7 or t==7:o&=~1
 if f==0 or t==0:o&=~2
 if f==116 or t==116:o&=~12
 if f==119 or t==119:o&=~4
 if f==112 or t==112:o&=~8
 return n,o,(f+t)//2 if abs(p)==1 and abs(t-f)==32 else-1
def L(b,s,c,e):
 o=[]
 for m in G(b,s,c,e):
  n,w,y=X(b,s,c,e,m)
  if not D(n,K(n,s),-s):o.append(m)
 return o
def E(b,s):
 z=0;h=[0,0];j=[[0]*8,[0]*8]
 for i in range(128):
  if i&136:continue
  p=b[i]
  if not p:continue
  t=abs(p);k=(i>>4)*8+(i&7);v=W[t]+Q[(t-1)*64+(k if p>0 else k^56)]
  if t==1:j[0 if p>0 else 1][i&7]+=1
  if t==3:h[0 if p>0 else 1]+=1
  if t==4 and((p>0 and i>>4==6)or(p<0 and i>>4==1)):v+=20
  z+=v if p>0 else-v
 if h[0]==2:z+=30
 if h[1]==2:z-=30
 for c in range(2):
  for f in range(8):
   if j[c][f]>1:z+=(j[c][f]-1)*(-10 if c==0 else 10)
 for k,p,d in((K(b,1),1,16),(K(b,-1),-1,-16)):
  if k<0:continue
  w=0
  for q in(d-1,d,d+1):
   t=k+q
   if not(t&136)and b[t]==p:w+=1
  z+=(w*12-12)*p
 return z*s
def O(b,s,m,t,k):
 def y(v):
  x=(v>>7)&127;u=b[x];q=0
  if u:q=10*W[abs(u)]-W[abs(b[v&127])]//10
  elif v==t:q=100000
  elif v in k:q=5000
  return-q
 return sorted(m,key=y)
class Y(Exception):pass
def J(b,s,c,e,a,d,pl):
 N[0]+=1
 if N[0]>B:raise Y
 v=E(b,s)
 if v>=d:return d
 if v>a:a=v
 o=D(b,K(b,s),-s)
 if o:x=L(b,s,c,e)
 else:
  x=[]
  for m in G(b,s,c,e):
   t=(m>>7)&127
   if b[t]or((m>>14)&7)or t==e:
    n,w,y=X(b,s,c,e,m)
    if not D(n,K(n,s),-s):x.append(m)
 for m in O(b,s,x,0,()):
  n,w,y=X(b,s,c,e,m);v=-J(n,-s,w,y,-d,-a,pl+1)
  if v>=d:return d
  if v>a:a=v
 return a
def R(b,s,c,e,d,a,f,pl,k,nm=1):
 N[0]+=1
 if N[0]>B:raise Y
 if d<=0:return J(b,s,c,e,a,f,pl)
 o=D(b,K(b,s),-s)
 if nm and d>=3 and not o:
  g=0
  for i in range(128):
   if i&136:continue
   p=b[i]
   if p and abs(p)not in(1,6):g=1;break
  if g:
   v=-R(b,-s,c,-1,d-3,-f,-f+1,pl+1,k,0)
   if v>=f:return f
 y=(b.tobytes(),s,c,e,d);t=T.get(y);u=0
 if t:
  u=t[2]
  if t[0]>=f and t[1]==1:return f
  if t[0]<=a and t[1]==2:return a
 m=L(b,s,c,e)
 if not m:
  if o:return-100000+pl
  return 0
 m=O(b,s,m,u,k[pl]if pl<len(k)else())
 z=-1000000;w=0;g=2;A=a
 for v in m:
  n,x,yy=X(b,s,c,e,v);q=-R(n,-s,x,yy,d-1+(1 if o else 0),-f,-A,pl+1,k)
  if q>z:z=q;w=v
  if q>A:
   A=q;g=0
   if A>=f:
    g=1
    if pl<len(k)and not b[(v>>7)&127]:k[pl]=k[pl][1:]+[v]if len(k[pl])>1 else[v]
    break
 T[y]=(z,g,w);return z
def C(f,l):
 b,s,c,e=F(f);r=[S(u[:2])|(S(u[2:4])<<7)|((("nbrq".index(u[4])+2)<<14)if len(u)==5 else 0)for u in l];N[0]=0;T.clear();k=[()for _ in range(64)];o=r[0];d=1
 while N[0]<B:
  try:
   z=[];a=-1000000
   for m in r:
    n,x,y=X(b,s,c,e,m);q=-R(n,-s,x,y,d-1,-1000000,-a,1,k)
    z.append((q,m))
    if q>a:a=q
  except Y:break
  z.sort(key=lambda x:-x[0]);o=z[0][1];d+=1
  if d>64:break
 v=(o>>14)&7;return Z(o&127)+Z((o>>7)&127)+("nbrq"[v-2]if v else"")
if __name__=="__main__":
 while 1:
  g=H("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":g=H("/move",{"game":g["game"],"move":C(g["fen"],g["legal_moves"])})
