// This file was generated by lezer-generator. You probably shouldn't edit it.
import {LRParser, LocalTokenGroup} from "@lezer/lr"
import {specializeKeyword, extendKeyword} from "./tokens"
export const parser = LRParser.deserialize({
  version: 14,
  states: "=vQYQPOOOOQO'#D|'#D|QYQPOOO!gQPO'#EXOOQO'#EU'#EUO!{QPO'#DXO#TQPO'#DQO#]QPO'#D{OOQO'#E]'#E]O#hQPO'#D`OOQO'#E^'#E^O$UQPO'#DaOOQO'#E_'#E_O$]QPO'#DbOOQO'#E`'#E`O$dQPO'#DdOOQO'#Ea'#EaO$kQPO'#DeOOQO'#Eb'#EbO$rQPO'#DfOOQO'#Dc'#DcOOQO'#Ec'#EcO$yQPO'#DgOOQO'#Ed'#EdO%iQPO'#DhOOQO'#Ef'#EfO%pQPO'#DiOOQO'#Eh'#EhO&YQPO'#DjOOQO'#Eo'#EoO&aQPO'#DuOOQO'#Ep'#EpO&lQPO'#DvOOQO'#Er'#ErO&wQPO'#DwOOQO'#Eu'#EuO'PQPO'#DxOOQO'#Ev'#EvO'XQPO'#DyOOQO'#Ew'#EwO'`QPO'#DzOOQO'#DP'#DPQ!bQPO'#D}Q'gQPOOOOQO-E7z-E7zOOQO'#EO'#EOO(qQPO,59nOOQO'#EQ'#EQO)eQPO,59lOOQO'#DU'#DUO)PQPO,59lOOQO-E8S-E8SO)lQPO,59sO+VQPO,59lO#sQPO,59lOOQO'#EX'#EXOOQO-E8V-E8VOOQO-E8Z-E8ZO,UQPO'#DVO-OOSO'#E}O-WOQO'#FROOQO'#DW'#DWO-`QPO'#E[OOQO'#DV'#DVOOQO'#E['#E[O.TQPO,59{OOQO-E8[-E8[O._QPO,59|OOQO-E8]-E8]OOQO,59|,59|O.sQPO,5:OOOQO-E8^-E8^OOQO,5:O,5:OO/XQPO,5:POOQO-E8_-E8_OOQO,5:P,5:PO/mQPO,5:QOOQO-E8`-E8`OOQO,5:Q,5:QO0RQPO,5:ROOQO-E8a-E8aOOQO,5:R,5:RO0gQPO,5:SOOQO-E8b-E8bO0xQPO,5:TOOQO-E8d-E8dO1ZQPO'#DmO2OQPO'#DVOOQO-E8f-E8fOOQO'#Dk'#DkO2vQPO,5:UOOQO-E8m-E8mOOQO-E8n-E8nO3UQPO,5:bOOQO-E8p-E8pO3ZQPO,5:cOOQO-E8s-E8sO3`QPO,5:dO3kQPO,5:eOOQO-E8t-E8tOOQO-E8u-E8uO3uQPO,5:fO4TQPO,5:iOOQO-E7{-E7{OOQO-E7|-E7|OOQO'#EP'#EPO5eQPO1G/YOOQO1G/Y1G/YO7RQPO'#DVOOQO-E8O-E8OO7]QPO'#ERO8QQPO1G/dOOQO'#ER'#ERO8xQPO1G/WO9SQPO1G/dOOQO'#EZ'#EZO9[QPO1G/eOOQO'#EV'#EVO9cQPO1G/_OOOO'#ES'#ESO9jOSO,5;iOOQO,5;i,5;iOOOO'#ET'#ETO9rOQO,5;mOOQO,5;m,5;mOOQO'#D['#D[OOQO'#D]'#D]O%WQPO,5;rO%WQPO,5;rOOQO-E8Y-E8YOOQO'#Ee'#EeO9zQPO1G/nOOQO'#Eg'#EgO:SQPO1G/oO:[QPO,5:XO:cQPO,5:XOOQO'#Do'#DoO%WQPO,5:YOOQO'#Dq'#DqOOQO'#Dr'#DrO:cQPO,5:[OOQO'#Ej'#EjO:jQPO,5:_OOQO'#Ek'#EkO:rQPO,5:`O:zQPO,5:WOOQO'#Em'#EmO;SQPO'#ElOOQO'#En'#EnO;ZQPO'#ElO;bQPO1G/pOOQO'#Eq'#EqO;pQPO1G/|O;{QPO1G/}O9cQPO1G0OO<WQPO1G0QOOQO-E7}-E7}O<fQPO'#EYO<nQPO7+%OOOQO-E8P-E8POOQO-E8X-E8XO<yQPO7+%POOQO-E8T-E8TO=TQPO'#FVOOQO'#FV'#FVO>nQPO'#DYOOQO7+$y7+$yOOOO-E8Q-E8QOOQO1G1T1G1TOOOO-E8R-E8ROOQO1G1X1G1XOOQO1G1^1G1^O@XQPO1G1^OOQO-E8c-E8cOOQO7+%Y7+%YOOQO-E8e-E8eOOQO7+%Z7+%ZOAoQPO1G/sO%WQPO1G/sOBZQPO1G/tOBuQPO1G/vO%WQPO1G/vOOQO-E8h-E8hOOQO1G/y1G/yOOQO-E8i-E8iOOQO1G/z1G/zOOQO'#Ei'#EiOCaQPO1G/rOOQO-E8k-E8kOOQO,5;W,5;WOOQO-E8l-E8lOOQO-E8j-E8jOOQO-E8o-E8oOOQO'#Es'#EsOCrQPO7+%iOOQO7+%i7+%iOOQO7+%j7+%jOC}QPO,5:tOOQO,5:t,5:tOOQO-E8W-E8WO#sQPO'#EWOD]QPO,59tOEvQPO7+%_OFbQPO7+%bOOQO-E8g-E8gOOQO-E8q-E8qOF|QPO<<ITOOQO,5:r,5:rOOQO-E8U-E8UOOQO'#Et'#EtOGRQPOAN>oOOQO'#DY'#DYOOQO-E8r-E8rOOQOG24ZG24ZPOQO,59t,59tO9cQPO1G/_OG^QPO,59sOGeQPO'#DXO%WQPO,5;rO%WQPO,5;rOGmQPO1G1^",
  stateData: "Gw~OqOS#nOS~OSkOUmOYwOZsO]YO^^O_`O`bOaeOb[OcgOeiOgWOjoOlqOoSOpuOuRO#oPO~OQ}OX!PO#p!ROu!{X#l!{X#o!{X~OoSOu!UO~OX!PO#p!RO~Ou!XO#l!oX#o!oX~OgWO#l!SX#o!SX~OoSOu![Ow!aO#r!]O#v!^O~O]YO~P#sOb[O~P#sO^^O~P#sO_`O~P#sO`bO~P#sOaeO#l!ZX#o!ZX~P#sOoSOu!aOw!aO#r!]O#v!^O~OcgO~P%WOeiO~P%WOoSOu!yOw!aO#r!]O#v!^O~OSkO~P%wOUmO#l!iX#o!iX~OjoOu#POw#PO~OlqOu#RO~OZsOu#TO~OpuO~P#sOYwO~P%wOSkOUmOYwOZsO]YO^^O_`O`bOaeOb[OcgOeiOgWOjoOlqOoSOpuOuRO~OQ}OR#]Ou#_Ow#_O~OP#gOoSOu#`Ow#cO#r!]O#v!^O~OX!PO~P)PO[#iO#l{a#o{ao{au{aw{a#r{a#v{a#{{a#|{a#}{a$O{af{ad{aX{ah{ai{a#p{a$P{a$Q{a$R{aV{aW{a~OX!PO~P#sOQ}OoyXuyXwyX#lyX#oyX#ryX#vyX#{yX#|yX#}yX$OyX~O}yXfyXdyXXyXhyXiyX#pyX$PyX$QyX$RyXVyXWyX~P+^O#s#kO#t#mO~O#w#nO#x#pO~O#{#qO#|#qO#}#rO$O#rOo#OXu#OXw#OX#l#OX#o#OX#r#OX#v#OX~O#l!Ta#o!Ta~P#sO#{#qO#|#qO#}#rO$O#rO#l!Ua#o!Ua~O#{#qO#|#qO#}#rO$O#rO#l!Wa#o!Wa~O#{#qO#|#qO#}#rO$O#rO#l!Xa#o!Xa~O#{#qO#|#qO#}#rO$O#rO#l!Ya#o!Ya~O#{#qO#|#qO#}#rO$O#rO#l!Za#o!Za~Of#vO#{#qO#|#qO#}#rO$O#rO~Od#xO#{#qO#|#qO#}#rO$O#rO~OX!POh$ROi$TO#p!RO#{#qO#|#qO#}#rO$O#rO$P#|O$Q$OO$R$PO~OX!POXyXhyXiyX#pyX#{yX#|yX#}yX$OyX$PyX$QyX$RyX~OV$WOW$YO#l!^a#o!^a~Ok$]O~Oh$RO~O[#iO#l!la#o!la~O#l!ma#o!ma~P#sOV$WOW$YO#l!na#o!na~O#oPOS!qaU!qaY!qaZ!qa]!qa^!qa_!qa`!qaa!qab!qac!qae!qag!qaj!qal!qao!qap!qau!qa#l!qa~OR#]OXvi#pvioviuviwvi#lvi#ovi#rvi#vvi}vi#{vi#|vi#}vi$Ovifvidvihviivi$Pvi$Qvi$RviVviWvi~Ou!{X}!{X~P+^O#{#qO#|#qO#}#rO$O#rOo!uXu!uXw!uX#l!uX#o!uX#r!uX#v!uX~O}$cOoyXuyXwyX#lyX#oyX#ryX#vyX#{yX#|yX#}yX$OyX~O#lti#oti~P#sOu!XO}$cO~OP#gO~P#sO[#iO~P#sO#s#kO#t$nO~O#w#nO#x$pO~Of#vOu$tO~Od#xOu$vO~OX!PO~P%WO#p!RO~P%WOh$ROu$}O~Oi$TOu%PO~OT%QOX!PO~OV$WO~P%wOW$YO~P%wOV$WOW$YO#l!^i#o!^i~Ok$]O#l!ji#o!ji~Oh$ROn%XOu%ZO~OV$WOW$YO#l!ni#o!ni~Ou!XOw%^O~O}$cO#l!Qq#o!Qq~O#l!Rq#o!Rq~P#sO#{#qO#|#qO#}#rO$O#rO}#yX#l#yX#o#yXo#yXu#yXw#yX#r#yX#v#yXf#yXd#yXX#yXh#yXi#yX#p#yX$P#yX$Q#yX$R#yXV#yXW#yX~O}%`O#l|X#o|Xo|Xu|Xw|X#r|X#v|X#{|X#||X#}|X$O|Xf|Xd|XX|Xh|Xi|X#p|X$P|X$Q|X$R|XV|XW|X~O#{#qO#|#qO#}#rO$O#rOo#ziu#ziw#zi#l#zi#o#zi#r#zi#v#zif#zid#ziX#zih#zii#zi#p#zi$P#zi$Q#zi$R#ziV#ziW#zi~O#{#qO#|#qO#}#rO$O#rOV!aiW!ai#l!ai#o!ai~O#{#qO#|#qO#}#rO$O#rOV!biW!bi#l!bi#o!bi~O#{#qO#|#qO#}#rO$O#rOV!diW!di#l!di#o!di~OT%QOV!`iW!`i#l!`i#o!`i~On%XOu%fOw%fO~Ou!XO}!|a#l!|a#o!|a~O}%`O#l|a#o|ao|au|aw|a#r|a#v|a#{|a#||a#}|a$O|af|ad|aX|ah|ai|a#p|a$P|a$Q|a$R|aV|aW|a~O#{#qO#|#qO#}#rO$O#rOV!aqW!aq#l!aq#o!aq~O#{#qO#|#qO#}#rO$O#rOV!dqW!dq#l!dq#o!dq~Om%iO~Om%iOu%mOw%mO~O}{a~P)lOoSOu%pO~O}#zi~P@XOwu~",
  goto: "3}#{PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP#|$RP$WP%R%b'O'v(sP(z)b$R$R$R$R$R$R)x)x)x$R$R$R$R)}*X*X*X*_*X*b*b*X*X$R$R$R$R$R$R$R*e*o*v+O+U+h+q+w+}-O-^-d-u-|.T.c.k.s.{/T/]/e/m/u/{0T0Z0c0i0s0y1T1^1g1o1w1}2V2]2c2k2sPPPPP2{PPP2{PPP3s'OVzOQ{VyOQ{UUOQ{[!bZv!c#U#h$gQ!g]Q!j_Q!maQ!pcQ!sfY#d!Q!S!V!W#eX$j#j$`%`%oQ!SRQ!WUQ#{!xQ$x#{R${$Q[!`Zv!c#U#h$gQ!e]Q!h_Q!kaQ!ncQ!qfQ!thQ!vjW!xlx$X$ZY#b!Q!S!V!W#eW$i#j$`%`%oS$q#s%rQ$r#tS$w#z#{Q$y#}Q$z$QQ%b$xQ%c${R%t%s!k!aZ]_acfhjlvx!Q!S!V!W!c#U#e#h#j#s#t#z#{#}$Q$X$Z$`$g$x${%`%o%r%sUyOQ{!k!aZ]_acfhjlvx!Q!S!V!W!c#U#e#h#j#s#t#z#{#}$Q$X$Z$`$g$x${%`%o%r%sS$l#j%oR%[$`p#s!`!e!h!k!n!q!t!v!x#b$r$w$y$z%b%cT%r$i%tp#t!`!e!h!k!n!q!t!v!x#b$r$w$y$z%b%cT%s$i%tVdOQ{Q!|lQ#XxT%T$X$ZX!{lx$X$ZR#}!xR$Q!xQQOS|Q#YR#YzS{OQR#Z{U!OR![#`R#[!OQ#^!OR$b#^Q!QRQ!VUW#a!Q!V#z$VQ#z!xR$V!yW#e!Q!S!V!WR$e#eQ#l!]R$m#lQ#o!^R$o#o!dTOQZ]_acfhjlvx{!Q!S!V!W!c#U#e#h#s#t#z#{#}$Q$X$Z$g$x${S!TT%q]%q#j$`%`%o%r%sQ#j!UQ$`#TU$h#j$`%oR%o%pQ%a$kR%h%aUVOQ{U!YV#f%]S#f!Q!SR%]$cS$d#c#fR%_$dS#h!Q!SR$f#hQ!cZQ#UvU#u!c#U$gR$g#hUXOQ{R!ZXUZOQ{R!dZU]OQ{R!f]U_OQ{R!i_UaOQ{R!laUcOQ{R!ocUfOQ{R!rfUhOQ{R!uhQ#w!tR$s#wUjOQ{R!wjQ#y!vR$u#yUlOQ{R!zlQ%R$VR%d%RQ$S!xQ$_#RT$|$S$_Q$U!xR%O$UQ$[!|Q$a#XT%V$[$aW$X!|#X$[$aR%S$XW$Z!|#X$[$aR%U$ZUnOQ{R!}nUpOQ{R#OpQ$^#PR%W$^UrOQ{R#QrQ%Y$_R%e%YQ%j%fR%l%jUtOQ{R#StUvOQ{R#VvUxOQ{R#Wx!k!_Z]_acfhjlvx!Q!S!V!W!c#U#e#h#j#s#t#z#{#}$Q$X$Z$`$g$x${%`%o%r%sS$k#j$`Q%g%`R%k%o",
  nodeNames: "⚠ ask at random if pressed else and or is while define with print forward turn color sleep play add from remove toList clear in not_in repeat times for to range call return Comment Program Command Assign Text ListAccess Number Op Expression String Call Arguments Comma Op Op AssignList Ask Clear Print Play Turtle Forward Turn Color Sleep Add Remove If Condition PressedCheck EqualityCheck NotEqualCheck Op ComparisonCheck Op Op InListCheck NotInListCheck Else Repeat For Define Return While ErrorInvalid",
  maxTerm: 141,
  nodeProps: [
    ["group", 53,"turtle"]
  ],
  skippedNodes: [0,33],
  repeatNodeCount: 42,
  tokenData: "1e~R!`OY%TYZ&XZp%Tpq&^qr&crs&nst&stw%Twx'[xz%Tz{'a{|'f|}'k}!O'p!O!P%T!P!Q'u!Q!R'z!R!S'z!S!T'z!T!U'z!U!V'z!V!W'z!W!X'z!X!Y'z!Y!Z'z!Z!['z![!^%T!^!_1U!_!`1Z!`!a1`!a#Q%T#RBn%TBnBo'kBoDf%TDfDg'zDgDh'zDhDi'zDiDj'zDjDk'zDkDl'zDlDm'zDmDn'zDnDo'zDoDp'zDpGl%TGlGm'zGmGn'zGnGo'zGoGp'zGpGq'zGqGr'zGrGs'zGsGt'zGtGu'zGuGv'zGv&FV%T&FV&FW'k&FW;'S%T;'S;=`&R<%l?Hb%T?Hb?Hc'k?HcO%T~%Y]u~OY%TZp%Ttw%Txz%T!O!P%T!Q!^%T!a#Q%T#RBn%TBo&FV%T&FW;'S%T;'S;=`&R<%l?Hb%T?HcO%T~&UP;=`<%l%T~&^O#o~~&cO#n~~&fP!_!`&i~&nO$P~~&sO#r~~&xSq~OY&sZ;'S&s;'S;=`'U<%lO&s~'XP;=`<%l&s~'aO#v~~'fO#{~~'kO#}~~'pO}~~'uO$O~~'zO#|~~(R}w~u~OY%TZp%Ttw%Txz%T!O!P+O!Q!R'z!R!S'z!S!T'z!T!U'z!U!V'z!V!W'z!W!X'z!X!Y'z!Y!Z'z!Z!['z![!^%T!a#Q%T#RBn%TBoDf%TDfDg'zDgDh'zDhDi'zDiDj'zDjDk'zDkDl'zDlDm'zDmDn'zDnDo'zDoDp'zDpGl%TGlGm'zGmGn'zGnGo'zGoGp'zGpGq'zGqGr'zGrGs'zGsGt'zGtGu'zGuGv'zGv&FV%T&FW;'S%T;'S;=`&R<%l?Hb%T?HcO%T~+T}u~OY%TZp%Ttw%Txz%T!O!P%T!Q!R.Q!R!S.Q!S!T.Q!T!U.Q!U!V.Q!V!W.Q!W!X.Q!X!Y.Q!Y!Z.Q!Z![.Q![!^%T!a#Q%T#RBn%TBoDf%TDfDg.QDgDh.QDhDi.QDiDj.QDjDk.QDkDl.QDlDm.QDmDn.QDnDo.QDoDp.QDpGl%TGlGm.QGmGn.QGnGo.QGoGp.QGpGq.QGqGr.QGrGs.QGsGt.QGtGu.QGuGv.QGv&FV%T&FW;'S%T;'S;=`&R<%l?Hb%T?HcO%T~.X}w~u~OY%TZp%Ttw%Txz%T!O!P%T!Q!R.Q!R!S.Q!S!T.Q!T!U.Q!U!V.Q!V!W.Q!W!X.Q!X!Y.Q!Y!Z.Q!Z![.Q![!^%T!a#Q%T#RBn%TBoDf%TDfDg.QDgDh.QDhDi.QDiDj.QDjDk.QDkDl.QDlDm.QDmDn.QDnDo.QDoDp.QDpGl%TGlGm.QGmGn.QGnGo.QGoGp.QGpGq.QGqGr.QGrGs.QGsGt.QGtGu.QGuGv.QGv&FV%T&FW;'S%T;'S;=`&R<%l?Hb%T?HcO%T~1ZO$R~~1`O#p~~1eO$Q~",
  tokenizers: [2, new LocalTokenGroup("_~RQYZXwxX~^O#x~~", 14, 131), new LocalTokenGroup("_~RQYZXrsX~^O#t~~", 14, 127)],
  topRules: {"Program":[0,34]},
  dynamicPrecedences: {"77":-10},
  specialized: [{term: 37, get: (value: any, stack: any) => (specializeKeyword(value, stack) << 1), external: specializeKeyword},{term: 37, get: (value: any, stack: any) => (extendKeyword(value, stack) << 1) | 1, external: extendKeyword, extend: true}],
  tokenPrec: 1784
})
