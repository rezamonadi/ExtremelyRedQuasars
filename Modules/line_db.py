def line_db(ymax, fs, fs1, ii):
    from numpy import array
    import matplotlib.pyplot as plt
    # some line wavelengths
    s6 = array([933.862,944.523])
    c3 = array([977.020,1175.71,1908.73])
    n3 = array([989.799, 1750.0])
    lyb = 1025.722
    o6 = array([1031.926,1037.617])
    s4 = array([1062.664,1073.518])
    n2 = array([1083.993,1084.580,1085.701,2142.0])
    p5 = array([1117.977,1128.008])
    si3 = array([1206.500,1892.03])
    lya = 1215.670
    he2 = 1640.4
    n4 = 1486.5
    #o4 = array([1397.21,1399.78,1404.79,1407.39])
    o4 = array([1401.157,1407.382])
    n5 = array([1238.821,1242.804])
    si2a = array([1190.416,1193.290,1194.500])
    si2b = array([1260.422,1264.738,1526.7066,1533.4310])
    #o1 = array([1302.1685,1305.0])
    o1 = array([1302.1685,1305.0])
    o1c = 1303.5
    #c2 = array([1334.532,1335.708])
    c2 = array([1334.532,1335.708,2326.0])
    c2c = 1335.0
    si4 = array([1393.755,1402.770])
    c4 = array([1548.195,1550.770])
    fe2 = array([1608.4511, 1786.7])
    fe3 = array([1122.52,1124.87,1128.72,1131.908,1895.46,1914.06,1926.30])
    o3 = 1664.
    al2 = array([1670.7874])
    al3 = array([1854.716,1862.7895])
    mg2 = array([2796.352,2803.531])
    
    # Set the size and aspect ratio of the output pdf plot (in inches) by inserting this command before all other plot commands:
    # This sets the axis ranges:
    plt.ylim(0.0,ymax)
#     plt.xlim(1145,1975)
#     plt.xlim(1145,1675)
    # This uses the wavelength data to draw all the light blue vertical lines in my plot to mark where different lines should be:
    plt.axvline(lya,c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(lyb,c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(he2,c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(o6[0],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(o6[1],c='c',lw=0.6,ls='--', alpha=0.5)
    #plt.axvline(si3[1],c='gold',lw=0.6,ls='--', alpha=1.0)
    plt.axvline(n5[0],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(n5[1],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(n3[1],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(c3[2],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(si2b[0],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(si2b[1],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(si2b[2],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(si2b[3],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(si4[0],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(si4[1],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(o4[0],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(o4[1],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(s4[0],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(s4[1],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(c4[0],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(c4[1],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(c2c,c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(fe2[1],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(fe3[0],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(fe3[1],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(fe3[2],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(fe3[3],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(fe3[4],c='c',lw=0.6,ls='--',alpha=0.5)
    plt.axvline(fe3[5],c='c',lw=0.6,ls='--',alpha=0.5)
    plt.axvline(fe3[6],c='c',lw=0.6,ls='--',alpha=0.5)
    plt.axvline(si3[1],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(o1c,c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(n4,c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(o3,c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(al3[0],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(al3[1],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(mg2[1],c='c',lw=0.6,ls='--', alpha=0.5)
    plt.axvline(mg2[0],c='c',lw=0.6,ls='--', alpha=0.5)
    # This inserts labels for most of the lines near the top of the plot window (where ymax = the top):
    plt.text(1197,  0.94*ymax,'Ly$\\alpha$',ha='center',va='center',fontsize=fs)
    plt.text(1240,  0.97*ymax,'NV',ha='center',va='center',fontsize=fs)
    plt.text(1264,  0.92*ymax,'SiII',ha='center',va='center',fontsize=fs)
    plt.text(1303,  0.95*ymax,'OI',ha='center',va='center',fontsize=fs)
    plt.text(1335,  0.95*ymax,'CII',ha='center',va='center',fontsize=fs)
    plt.text(1399,  0.95*ymax,'SiIV',ha='center',va='center',fontsize=fs1)
    plt.text(1403,  0.9*ymax,'OIV]',ha='center',va='center',fontsize=fs1)
    plt.text(1486,  0.95*ymax,'NIV]',ha='center',va='center',fontsize=fs)
    plt.text(1527,  0.9*ymax,'SiII',ha='center',va='center',fontsize=fs)
    plt.text(1549,  0.95*ymax,'CIV',ha='center',va='center',fontsize=fs)
    if(ii<3):
        plt.text(1743,  0.93*ymax,'NIII]',ha='center',va='center',fontsize=fs)
        plt.text(1790,  0.93*ymax,'FeII',ha='center',va='center',fontsize=fs)
        plt.text(1625,  0.95*ymax,'HeII',ha='center',va='center',fontsize=fs)
        plt.text(1672,  0.95*ymax,'OIII]',ha='center',va='center',fontsize=fs)
        plt.text(1859,  0.95*ymax,'AlIII',ha='center',va='center',fontsize=fs)
        plt.text(1888,  0.9*ymax,'SiIII]',ha='center',va='center',fontsize=fs)
        plt.text(1909,  0.95*ymax,'CIII]',ha='center',va='center',fontsize=fs)
        plt.text(1926,  0.9*ymax,'FeIII',ha='center',va='center',fontsize=fs)
