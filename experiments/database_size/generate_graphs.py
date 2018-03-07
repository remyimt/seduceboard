import sys
import matplotlib.pyplot as plt


DATA = [(0, 24), (86400, 32), (88200, 32), (90000, 7672), (91800, 7672), (93600, 15336), (95400, 15336), (97200, 22968), (99000, 22968), (100800, 30600), (102600, 30600), (104400, 38264), (106200, 38264), (108000, 31000), (109800, 31000), (111600, 38640), (113400, 38640), (115200, 46248), (117000, 46248), (118800, 53920), (120600, 53920), (122400, 61568), (124200, 61568), (126000, 53776), (127800, 53776), (129600, 61368), (131400, 61368), (133200, 69248), (135000, 69248), (136800, 76896), (138600, 76896), (140400, 84544), (142200, 69216), (144000, 76840), (145800, 76840), (147600, 84504), (149400, 84504), (151200, 92144), (153000, 92144), (154800, 99832), (156600, 99832), (158400, 107472), (160200, 91544), (162000, 100080), (163800, 100080), (165600, 107712), (167400, 107712), (169200, 115344), (171000, 115344), (86400, 115344), (172800, 115352), (174600, 115352), (176400, 123016), (178200, 123016), (180000, 130648), (181800, 130648), (183600, 122888), (185400, 122888), (187200, 130616), (189000, 130616), (190800, 138232), (192600, 138232), (194400, 145864), (196200, 145864), (198000, 153576), (199800, 153576), (201600, 146008), (203400, 146008), (205200, 153680), (207000, 153680), (208800, 161352), (210600, 161352), (212400, 168960), (214200, 168960), (216000, 176624), (217800, 176624), (219600, 168792), (221400, 168792), (223200, 176464), (225000, 176464), (226800, 184120), (228600, 184120), (230400, 191752), (232200, 191752), (234000, 199552), (235800, 183656), (237600, 192520), (239400, 192520), (241200, 200184), (243000, 200184), (244800, 207856), (246600, 207856), (248400, 215544), (250200, 215544), (252000, 223192), (253800, 241624), (255600, 214896), (257400, 214896), (172800, 214896), (259200, 214896), (261000, 214896), (262800, 222624), (264600, 222624), (266400, 230272), (268200, 230272), (270000, 237896), (271800, 237896), (273600, 245496), (275400, 230696), (277200, 238304), (279000, 238304), (280800, 246096), (282600, 246096), (284400, 253704), (286200, 253704), (288000, 261352), (289800, 261352), (291600, 268944), (293400, 268944), (295200, 261224), (297000, 261224), (298800, 268848), (300600, 268848), (302400, 276480), (304200, 276480), (306000, 284152), (307800, 284152), (309600, 291792), (311400, 276704), (313200, 284808), (315000, 284808), (316800, 292432), (318600, 292432), (320400, 300080), (322200, 300080), (324000, 307728), (325800, 307728), (327600, 315504), (329400, 315504), (331200, 307616), (333000, 307616), (334800, 315280), (336600, 315280), (338400, 322968), (340200, 322968), (342000, 330616), (343800, 330616), (259200, 330616), (345600, 330616), (347400, 330616), (349200, 338288), (351000, 322672), (352800, 330264), (354600, 330264), (356400, 337872), (358200, 337872), (360000, 345496), (361800, 345496), (363600, 353128), (365400, 353128), (367200, 360792), (369000, 360792), (370800, 353312), (372600, 353312), (374400, 361040), (376200, 361040), (378000, 368664), (379800, 368664), (381600, 376320), (383400, 376320), (385200, 383944), (387000, 368544), (388800, 403832), (390600, 403832), (392400, 411496), (394200, 411496), (396000, 419200), (397800, 419200), (399600, 426840), (401400, 426840), (403200, 434488), (405000, 418688), (406800, 426360), (408600, 426360), (410400, 434016), (412200, 434016), (414000, 441672), (415800, 441672), (417600, 449304), (419400, 449304), (421200, 456952), (423000, 456952), (424800, 448880), (426600, 448880), (428400, 456528), (430200, 456528), (345600, 456528), (432000, 458576), (433800, 458576), (435600, 464192), (437400, 464192), (439200, 471800), (441000, 471800), (442800, 479416), (444600, 479416), (446400, 471920), (448200, 471920), (450000, 479528), (451800, 479528), (453600, 487176), (455400, 487176), (457200, 494832), (459000, 494832), (460800, 502512), (462600, 502512), (464400, 496120), (466200, 496120), (468000, 503776), (469800, 503776), (471600, 511416), (473400, 511416), (475200, 519216), (477000, 519216), (478800, 526904), (480600, 511384), (482400, 519000), (484200, 519000), (486000, 526608), (487800, 526608), (489600, 534248), (491400, 534248), (493200, 541880), (495000, 541880), (496800, 549528), (498600, 549528), (500400, 541344), (502200, 541344), (504000, 548984), (505800, 548984), (507600, 556656), (509400, 556656), (511200, 564280), (513000, 564280), (514800, 571920), (516600, 571920), (432000, 556048), (518400, 556056), (520200, 556056), (522000, 563824), (523800, 563824), (525600, 571536), (527400, 571536), (529200, 579136), (531000, 579136), (532800, 586728), (534600, 586728), (536400, 594360), (538200, 594360), (540000, 588536), (541800, 588536), (543600, 596176), (545400, 596176), (547200, 603824), (549000, 603824), (550800, 611504), (552600, 611504), (554400, 619144), (556200, 619144), (558000, 611232), (559800, 611232), (561600, 618888), (563400, 618888), (565200, 626560), (567000, 626560), (568800, 634320), (570600, 634320), (572400, 641968), (574200, 641968), (576000, 633944), (577800, 633944), (579600, 641584), (581400, 641584), (583200, 649216), (585000, 649216), (586800, 656896), (588600, 656896), (590400, 664584), (592200, 648944), (594000, 656608), (595800, 656608), (597600, 664272), (599400, 664272), (601200, 671952), (603000, 671952), (518400, 671952), (604800, 671960), (606600, 671960), (608400, 679592), (610200, 679592), (612000, 687232), (613800, 687232), (615600, 680784), (617400, 680784), (619200, 688512), (621000, 688512), (622800, 696152), (624600, 696152), (626400, 703800), (628200, 703800), (630000, 711472), (631800, 711472), (633600, 703944), (635400, 703944), (637200, 711560), (639000, 711560), (640800, 719224), (642600, 719224), (644400, 726904), (646200, 726904), (648000, 734536), (649800, 734536), (651600, 726728), (653400, 726728), (655200, 734384), (657000, 734384), (658800, 742072), (660600, 742072), (662400, 749760), (664200, 749760), (666000, 757552), (667800, 741584), (669600, 749248), (671400, 749248), (673200, 756912), (675000, 756912), (676800, 764560), (678600, 764560), (680400, 772224), (682200, 772224), (684000, 779880), (685800, 779880), (687600, 1195128), (689400, 1227896), (604800, 1293432)]
BLOCK_SIZE = 4096

if __name__ == "__main__":
    sorted_data = sorted(DATA, key=lambda e: e[0])
    sorted_data_bytes = [(t, d * BLOCK_SIZE) for (t, d) in sorted_data]

    x_data = [t for (t, d) in sorted_data_bytes]
    y_data = [d for (t, d) in sorted_data_bytes]

    # x_data_labels = ["%s" % (x / (1024 * 1024)) for x in x_data]
    # y_data_labels = ["%s" % (y / (24 * 3600)) for y in y_data]

    x_ticks = [0, 1, 2, 3, 4, 5, 6, 7]
    x_ticks_str = ["%s" % s for s in x_ticks]
    x_ticks_values = [x * (24 * 3600) for x in x_ticks]

    y_ticks = [0, 100, 200, 300, 400, 500, 600, 700]
    y_ticks_str = ["%s" % s for s in y_ticks]
    y_ticks_values = [y * (1000 * 1000 * 10) for y in y_ticks]

    plt.xticks(x_ticks_values, x_ticks_str)
    plt.yticks(y_ticks_values, y_ticks_str)

    plt.plot(x_data, [d for (t, d) in sorted_data_bytes], 'b-')
    axes = plt.axes()

    plt.show()

    sys.exit(0)