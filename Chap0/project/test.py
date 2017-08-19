# -*- coding: utf-8 -*-
"""
Created on Mon Aug 07 10:59:38 2017

@author: acera
"""

import numpy as np

print "="*80

print """
\t                        Problem description:
\t   A square plate with unity thickness is subjected to a constant 
\tpressure on one side and it is clamped on the other side. The m-
\taganitude of the pressure is 20 and dircetion is along the z axis.
\tThe material of the plate is steel, which indicated that possion 
\tration is 0.3 and the elasitc modulus is 200e6.
\t   This script is to solve the plate problem with finite element 
\tusing isoparametric element. The result only cover the static 
\tanalysis.Firstly, let's give some geometric parameter to the plane.
"""

def feglqd1(ngl):
    point1=np.zeros((ngl,1))
    weight1=np.zeros((ngl,1))
    if ngl==1:
        point1=np.array([0])
        weight1=np.array([2])
    elif ngl==2:
        point1=np.array([[-0.57735],[0.57735]])
        weight1=np.array([[1],[1]])
    else:
        point1=np.array([[-0.7746],[0],[0.7746]])
        weight1=np.array([[0.55556],[0.88889],[0.55556]])
    
    return point1,weight1

def feglqd2(nglx,ngly):
    # derive the sample point and weight coefficient
    if nglx > ngly:
        ngl = nglx
    else:
        ngl = ngly
    point2=np.zeros((ngl,2))
    weight2=np.zeros((ngl,2))
    pointx,weightx=feglqd1(nglx)
    for i in range(nglx):
        point2[i,0]=pointx[i]
        weight2[i,0]=weightx[i]
    pointy,weighty=feglqd1(ngly)
    for j in range(ngly):
        point2[i,1]=pointy[i]
        weight2[i,1]=weighty[i]
    return point2,weight2

def fematiso(ipt,emodule,possion):
    # compute of propety martix
    # if ipt=1-plate stress problem
    # if ipt=2-plate strain problem
    if ipt==1:
        matmtrx=emodule/(1-possion*possion)*np.array([
                [1,possion,0],[possion,1,0],[0,0,(1-possion)/2]])
    else:
        matmtrx=emodule/((1+possion)*(1-2*possion))*np.array([
                [(1-possion),possion,0],[possion,(1-possion),0],[
                        0,0,(1-2*possion)/2]])
    return matmtrx
                
def feisoq4(r,s,el):
    # derive shape function, dhdr and dhds of bilinear element
    el2=el*el/4
    shape4=[1/(4*el2)*(el/2-r)*(el/2-s),1/(4*el2)*(el/2+r)*(el/2-s),
            1/(4*el2)*(el/2+r)*(el/2+s),1/(4*el2)*(el/2-r)*(el/2+s)]
    dhdr=[-1/(4*el2)*(el/2-s),1/(4*el2)*(el/2-s),
          1/(4*el2)*(el/2+s),-1/(4*el2)*(el/2+s)]
    dhds=[-1/(4*el2)*(el/2-r),-1/(4*el2)*(el/2+r),
          1/(4*el2)*(el/2+r),1/(4*el2)*(el/2-r)]
    return shape4,dhdr,dhds

def fekine2d(nnel,dhdx,dhdy,eodf):
    kinmtx2=np.zeros((3,edof))
    for j in range(nnel):
        i1=j*3
        i2=i1+1
        kinmtx2[0,i1]=dhdx[j]
        kinmtx2[1,i2]=dhdy[j]
        kinmtx2[2,i1]=dhdy[j]
        kinmtx2[2,i2]=dhdx[j]
    return kinmtx2
    

def fejacob2(nnel,dhdr,dhds,xcoord,ycoord):
    #compute the jacobin martix
    jacob2=np.zeros((2,2))
    for i in range(nnel):
        jacob2[0,0]=jacob2[0,0]+dhdr[i]*xcoord[i]
        jacob2[0,1]=jacob2[0,1]+dhdr[i]*ycoord[i]
        jacob2[1,0]=jacob2[1,0]+dhds[i]*xcoord[i]
        jacob2[1,1]=jacob2[1,1]+dhds[i]*ycoord[i]
    return jacob2

def federiv2(nnel,dhdr,dhds,invjacob):
    # compute dhdx and dhdy
    dhdy=[0]*nnel;dhdx=[0]*nnel
    for i in range(nnel):
        dhdx[i]=invjacob[0,0]*dhdr[i]+invjacob[0,1]*dhds[i]
        dhdy[i]=invjacob[1,0]*dhdr[i]+invjacob[1,1]*dhds[i]
    return dhdx,dhdy

def fekinepb(nnel,dhdx,dhdy):
    for i in range(nnel):
        i1=i*3
        i2=i1+1
        i3=i2+1
        kinmtpb[0,i1]=dhdx[i]
        kinmtpb[1,i2]=dhdy[i]
        kinmtpb[2,i1]=dhdy[i]
        kinmtpb[2,i2]=dhdx[i]
        kinmtpb[2,i3]=0
    return kinmtpb

def fekineps(nnel,dhdx,dhdy,shape):
    for i in range(nnel):
        i1=i*3
        i2=i1+1
        i3=i2+1
        kinmtps[0,i1]=-shape[i]
        kinmtps[0,i3]=dhdx[i]
        kinmtps[1,i2]=-shape[i]
        kinmtps[1,i3]=dhdy[i]
    return kinmtps
    
def feeldof(nd,nnel,ndof):
    # derive index
    k=0
    for i in range(nnel):
        start=(nd[i]-1)*ndof
        for j in range(ndof):
            index[k]=start+j+1
            k+=1
    return index

def feasmbl1(kk,k,index):
    edof=len(index)
    for i in range(edof):
        ii=int(index[i])-1
        for j in range(edof):
            jj=int(index[j])-1
            kk[ii,jj]=kk[ii,jj]+k[i,j]
    return kk

def feaplyc2(kk,ff,bcdof,bcval):
    n=len(bcdof)
    sdof=len(ff)
    for i in range(n):
        c=bcdof[i]
        c=c-1
        for j in range(sdof):
            kk[c,j]=0
        kk[c,c]=1
        ff[c]=bcval[i]
    return kk,ff
    

def element_1_calculate(nl):

    #if element_type == 1:
    element_type == 1
    nnel=3;ndof=3;
    nnode=nl*nl
    el=lenght/(nl-1)
    nel=(nl-1)*(nl-1)*2
    sdof=nnode*ndof
    edof=nnel*ndof
    print """
\t    To solve the problem, the plane is discreted in %s elements, 
\tand each element has 3 nodes. Totally, there are %s nodes and the 
\tdof of the each node is 3. Thus, solution will include %s value."""% (nel,nnode,sdof)
    emodule=200e6
    possion=0.3
    t=0.1
    nglxb=2;nglyb=2
    nglxs=1;nglys=1
    
    # global coordinary
    gcoord=np.zeros((nnode,2))
    for i in range(nl):
        for j in range(nl):
            gcoord[j+i*nl,0]=j*el
            gcoord[j+i*nl,1]=i*el
            
    # nodes connectivity
    nodes=np.zeros((nel,3))
    j=1;k=1
    for i in range(1,nel,2):
        nodes[i,0]=j+j/nl
        nodes[i,1]=j+nl+1+j/nl
        nodes[i,2]=j+nl+j/nl
        j+=1
    for i in range(0,nel,2):
        nodes[i,0]=k+k/nl
        nodes[i,1]=k+k/nl+1
        nodes[i,2]=k+k/nl+1+nl
        k+=1
        
    # apply boundary condition
    bcindex=[0]*nl
    if side1==1:
        for i in range(nl):
            bcindex[i]=i+1
    elif side1==2:
        for i in range(nl):
            bcindex[i]=(i+1)*nl
    elif side1==3:
        for i in range(nl):
            bcindex[i]=nl*nl-i
        bcindex=sorted(bcindex)
    else:
        for i in range(nl):
            bcindex[i]=1+i*nl
    bcindex=list(np.subtract(np.multiply(bcindex,3),[2]*nl))
    a=list(np.add(bcindex,[1]*nl))
    b=list(np.add(bcindex,[2]*nl))
    bcdof=sorted(bcindex+a+b)
    
    bcval=[0]*nl*3
    
    # initialization
    ff=np.zeros((sdof,1))
    kk=np.zeros((sdof,sdof))
    disp=np.zeros((sdof,1))
    index=np.zeros((edof,1))
    kinmtpb=np.zeros((3,edof))
    matmtpb=np.zeros((3,3))
    kinmtps=np.zeros((2,edof))
    matmtps=np.zeros((2,2))
    jacob2=np.zeros((2,2))
    nd=[0]*3;xcoord=[0]*3;ycoord=[0]*3
    shape=[0]*nnel
    dhdr=[0]*3;dhds=[0]*3
    
    #apply force
    ffindex=[0]*nl
    if side2==1:
        for i in range(nl):
            ffindex[i]=i+1
    elif side2==2:
        for i in range(nl):
            ffindex[i]=(i+1)*nl
    elif side2==3:
        for i in range(nl):
            ffindex[i]=nl*nl-i
        ffindex=sorted(ffindex)
    else:
        for i in range(nl):
            ffindex[i]=1+i*nl
    ffindex=np.multiply(ffindex,3)
    for i in range(nl):
        ff[ffindex[i]-1,0]=force*lenght/nl
    
    # numerical compute
    for iel in range(nel):
        for i in range(nnel):
            nd[i]=nodes[iel,i]
            xcoord[i]=gcoord[int(nd[i])-1,0]
            ycoord[i]=gcoord[int(nd[i])-1,1]
        k=np.zeros((edof,edof))
        kb=np.zeros((edof,edof))
        ks=np.zeros((edof,edof))
        
        matmtpb=fematiso(1,emodule,possion)*t*t*t/12
        
        points,weights=feglqd2(nglxs,nglys)
        shearm=0.5*emodule/(1+possion)
        matmtps=shearm*5/6*t*np.array([[1,0],[0,1]])
    
        A=0.5*(xcoord[1]*ycoord[2]+ycoord[1]*xcoord[0]+xcoord[2]*ycoord[0]-
               xcoord[1]*ycoord[0]-xcoord[0]*ycoord[2]-xcoord[2]*ycoord[1])
        
        pointb,weightb=feglqd2(nglxb,nglyb)
        
        for intx in range(nglxb):
            x=pointb[intx,0]
            wtx=weightb[intx,0]
            for inty in range(nglyb):
                y=pointb[inty,1]
                wty=weightb[inty,1]
                shape[0]=1/(2*A)*((xcoord[1]*ycoord[2]-xcoord[2]*ycoord[1])+
                     (ycoord[1]-ycoord[2])*x+(xcoord[2]-xcoord[1])*y)
                shape[1]=1/(2*A)*((xcoord[2]*ycoord[0]-xcoord[0]*ycoord[2])+
                     (ycoord[2]-ycoord[0])*x+(xcoord[0]-xcoord[2])*y)
                shape[2]=1/(2*A)*((xcoord[0]*ycoord[1]-xcoord[1]*ycoord[0])+
                     (ycoord[0]-ycoord[1])*x+(xcoord[1]-xcoord[0])*y)
                
                dhdr[0]=1/(2*A)*(ycoord[1]-ycoord[2]) 
                dhdr[1]=1/(2*A)*(ycoord[2]-ycoord[0])
                dhdr[2]=1/(2*A)*(ycoord[0]-ycoord[1])
                
                dhds[0]=1/(2*A)*(xcoord[2]-xcoord[1])
                dhds[1]=1/(2*A)*(xcoord[0]-xcoord[2])
                dhds[2]=1/(2*A)*(xcoord[1]-xcoord[0])
                
                jacob2=fejacob2(nnel,dhdr,dhds,xcoord,ycoord)
                jacobinv=np.linalg.inv(jacob2)
                jacobdet=np.linalg.det(jacob2)
                
                dhdx,dhdy=federiv2(nnel,dhdr,dhds,jacobinv)
                kinmtpb=fekinepb(nnel,dhdx,dhdy)
                zi1=np.dot(kinmtpb.T,matmtpb)
                zi=np.dot(zi1,kinmtpb)
                kb=kb+zi*wtx*wty*jacobdet
                
        for intx in range(nglxs):
            x=points[intx,0]
            wtx=weights[intx,0]
            for inty in range(nglys):
                y=points[inty,1]
                wty=weights[inty,1]
                
                shape[0]=1/(2*A)*((xcoord[1]*ycoord[2]-xcoord[2]*ycoord[1])+
                     (ycoord[1]-ycoord[2])*x+(xcoord[2]-xcoord[1])*y)
                shape[1]=1/(2*A)*((xcoord[2]*ycoord[0]-xcoord[0]*ycoord[2])+
                     (ycoord[2]-ycoord[0])*x+(xcoord[0]-xcoord[2])*y)
                shape[2]=1/(2*A)*((xcoord[0]*ycoord[1]-xcoord[1]*ycoord[0])+
                     (ycoord[0]-ycoord[1])*x+(xcoord[1]-xcoord[0])*y)
                
                dhdr[0]=1/(2*A)*(ycoord[1]-ycoord[2]) 
                dhdr[1]=1/(2*A)*(ycoord[2]-ycoord[0])
                dhdr[2]=1/(2*A)*(ycoord[0]-ycoord[1])
                
                dhds[0]=1/(2*A)*(xcoord[2]-xcoord[1])
                dhds[1]=1/(2*A)*(xcoord[0]-xcoord[2])
                dhds[2]=1/(2*A)*(xcoord[1]-xcoord[0])
                
                jacob2=fejacob2(nnel,dhdr,dhds,xcoord,ycoord)
                jacobdet=np.linalg.det(jacob2)
                jacobinv=np.linalg.inv(jacob2)
                
                dhdx,dhdy=federiv2(nnel,dhdr,dhds,jacobinv)
                kinmtps=fekineps(nnel,dhdx,dhdy,shape)
                zj1=np.dot(kinmtps.T,matmtps)
                zj=np.dot(zj1,kinmtps)
                ks=ks+zj*wtx*wty*jacobdet
                
        k=kb+ks
        index=feeldof(nd,nnel,ndof)
        kk=feasmbl1(kk,k,index)
        
    kk,ff=feaplyc2(kk,ff,bcdof,bcval)
    disp=np.dot(np.linalg.inv(kk),ff)
    dispmax=max(disp)
    print "\n\tThe displacement of each dof is shown below:\n"
    print disp
    print dispmax
    
    print "="*80
    
def element_2_calculate(nl):

    element_type=2:
    nnel=4;ndof=3
    nnode=nl*nl
    el=lenght/(nl-1)
    nel=(nl-1)*(nl-1)
    sdof=nnode*ndof
    edof=nnel*ndof
    print """
\t    To solve the problem, the plane is discreted in %s elements, 
\tand each element has 4 nodes. Totally, there are %s nodes and the 
\tdof of the each node is 3. Thus, solution will include %s value."""% (nel,nnode,sdof)
    emodule=200e6
    possion=0.3
    t=0.1
    nglxb=2;nglyb=2
    nglxs=1;nglys=1
    
    # global coordinary
    gcoord=np.zeros((nnode,2))
    for i in range(nl):
        for j in range(nl):
            gcoord[j+i*nl,0]=j*el
            gcoord[j+i*nl,1]=i*el
    # nodes connectivity
    nodes=np.zeros((nel,4))
    for i in range(nel):
        j=i/(nl-1)
        nodes[i,0]=i+1+j
        nodes[i,1]=i+2+j
        nodes[i,2]=i+2+nl+j
        nodes[i,3]=i+1+nl+j
    
    # set boundary condition
    bcindex=[0]*nl
    if side1==1:
        for i in range(nl):
            bcindex[i]=i+1
    elif side1==2:
        for i in range(nl):
            bcindex[i]=(i+1)*nl
    elif side1==3:
        for i in range(nl):
            bcindex[i]=nl*nl-i
        bcindex=sorted(bcindex)
    else:
        for i in range(nl):
            bcindex[i]=1+i*nl
    bcindex=list(np.subtract(np.multiply(bcindex,3),[2]*nl))
    a=list(np.add(bcindex,[1]*nl))
    b=list(np.add(bcindex,[2]*nl))
    bcdof=sorted(bcindex+a+b)
    
    bcval=[0]*nl*3
        
    # initialization
    ff=np.zeros((sdof,1))
    kk=np.zeros((sdof,sdof))
    disp=np.zeros((sdof,1))
    index=np.zeros((edof,1))
    kinmtpb=np.zeros((3,edof))
    matmtpb=np.zeros((3,3))
    kinmtps=np.zeros((2,edof))
    matmtps=np.zeros((2,2))
    nd=[0]*4;xcoord=[0]*4;ycoord=[0]*4
    jacob2=np.zeros((2,2))
    
     # apply force
    ffindex=[0]*nl
    if side2==1:
        for i in range(nl):
            ffindex[i]=i+1
    elif side2==2:
        for i in range(nl):
            ffindex[i]=(i+1)*nl
    elif side2==3:
        for i in range(nl):
            ffindex[i]=nl*nl-i
        ffindex=sorted(ffindex)
    else:
        for i in range(nl):
            ffindex[i]=1+i*nl
    ffindex=np.multiply(ffindex,3)
    for i in range(nl):
        ff[ffindex[i]-1,0]=force*lenght/nl
    
    # derive sample point and weighted coefficient
    pointb,weightb=feglqd2(nglxb,nglyb)
    matmtpb=fematiso(1,emodule,possion)*t*t*t/12
    
    points,weights=feglqd2(nglxs,nglys)
    shearm=0.5*emodule/(1+possion)
    matmtps=shearm*5/6*t*np.array([[1,0],[0,1]])
    
    #this is for text
    
    # numerical compute
    for iel in range(nel):
        for i in range(nnel):
            nd[i]=nodes[iel,i]
            xcoord[i]=gcoord[int(nd[i])-1,0]
            ycoord[i]=gcoord[int(nd[i])-1,1]
        k=np.zeros((edof,edof))
        kb=np.zeros((edof,edof))
        ks=np.zeros((edof,edof))
        for intx in range(nglxb):
            x=pointb[intx,0]
            wtx=weightb[intx,0]
            for inty in range(nglyb):
                y=pointb[inty,1]
                wty=weightb[inty,1]
                shape,dhdr,dhds=feisoq4(x,y,el)
                jacob2=fejacob2(nnel,dhdr,dhds,xcoord,ycoord)
                jacobdet=np.linalg.det(jacob2)
                jacobinv=np.linalg.inv(jacob2)
                dhdx,dhdy=federiv2(nnel,dhdr,dhds,jacobinv)
                kinmtpb=fekinepb(nnel,dhdx,dhdy)
                zi1=np.dot(kinmtpb.T,matmtpb)
                zi=np.dot(zi1,kinmtpb)
                kb=kb+zi*wtx*wty*jacobdet
        for intx in range(nglxs):
            x=points[intx,0]
            wtx=weights[intx,0]
            for inty in range(nglys):
                y=points[inty,1]
                wty=weights[inty,1]
                shape,dhdr,dhds=feisoq4(x,y,el)
                jacob2=fejacob2(nnel,dhdr,dhds,xcoord,ycoord)
                jacobdet=np.linalg.det(jacob2)
                jacobinv=np.linalg.inv(jacob2)
                dhdx,dhdy=federiv2(nnel,dhdr,dhds,jacobinv)
                kinmtps=fekineps(nnel,dhdx,dhdy,shape)
                zj1=np.dot(kinmtps.T,matmtps)
                zj=np.dot(zj1,kinmtps)
                ks=ks+zj*wtx*wty*jacobdet
        k=kb+ks
        index=feeldof(nd,nnel,ndof)
        kk=feasmbl1(kk,k,index)

    kk,ff=feaplyc2(kk,ff,bcdof,bcval)
    
    test1=np.linalg.inv(kk)
    test2=np.linalg.det(kk)
    
    disp=np.dot(np.linalg.inv(kk),ff)
    print "\n\tThe displacement of each dof is shown below:"
    print disp
    dispmax=max(disp)
    print dispmax
    print "="*80

def main():
    lenght = 1
    side1 = 1
    side2 = 3
    force = 20

    for nl in range(1,10):
        element_1_calculate()
        element_2_calculate()

if __name__ == '__main__':
    main()


    