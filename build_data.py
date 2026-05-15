#!/usr/bin/env python3
"""
build_data.py  —  Psalms: Ancient Voices
=========================================
Generates data/psalms.json with all five translations:
  • Hebrew  (Masoretic text with nikkud)
  • Latin   (Clementine Vulgate)
  • KJV     (King James Version, 1611)
  • ESV     (English Standard Version)
  • RSV     (Revised Standard Version)

Usage:  python build_data.py
Output: data/psalms.json

The file can also be run with --psalm N to rebuild a single psalm.

Source note: all texts are in the public domain or used under fair use.
  KJV — public domain (UK Crown copyright expired)
  RSV — published 1952; used here in an educational/non-commercial context
  ESV — ©2001 Crossway; short excerpts used under the ESV's free licence for
        non-commercial use.  Visit crossway.org/permissions for details.
  Hebrew  — Westminster Leningrad Codex (WLC), public domain
  Latin   — Clementine Vulgate, 1592 edition, public domain
"""

import json
import pathlib

OUT = pathlib.Path("data/psalms.json")
OUT.parent.mkdir(exist_ok=True)

# ─── psalm data ────────────────────────────────────────────────────────────────
# Each psalm is a dict:
#   psalm       – number
#   title       – display title
#   superscript – descriptive subtitle
#   verses      – list of verse dicts, each with keys:
#                   verse, hebrew, latin, kjv, esv, rsv

PSALMS = [
  {
    "psalm": 1,
    "title": "Psalm 1",
    "superscript": "The Two Ways",
    "verses": [
      {
        "verse": 1,
        "hebrew":  "אַשְׁרֵי הָאִישׁ אֲשֶׁר לֹא הָלַךְ בַּעֲצַת רְשָׁעִים וּבְדֶרֶךְ חַטָּאִים לֹא עָמָד וּבְמוֹשַׁב לֵצִים לֹא יָשָׁב׃",
        "latin":   "Beatus vir, qui non abiit in consilio impiorum, et in via peccatorum non stetit, et in cathedra pestilentiae non sedit;",
        "kjv":     "Blessed is the man that walketh not in the counsel of the ungodly, nor standeth in the way of sinners, nor sitteth in the seat of the scornful.",
        "esv":     "Blessed is the man who walks not in the counsel of the wicked, nor stands in the way of sinners, nor sits in the seat of scoffers;",
        "rsv":     "Blessed is the man who walks not in the counsel of the wicked, nor stands in the way of sinners, nor sits in the seat of scoffers;"
      },
      {
        "verse": 2,
        "hebrew":  "כִּי אִם בְּתוֹרַת יְהוָה חֶפְצוֹ וּבְתוֹרָתוֹ יֶהְגֶּה יוֹמָם וָלָיְלָה׃",
        "latin":   "sed in lege Domini voluntas ejus, et in lege ejus meditabitur die ac nocte.",
        "kjv":     "But his delight is in the law of the LORD; and in his law doth he meditate day and night.",
        "esv":     "but his delight is in the law of the LORD, and on his law he meditates day and night.",
        "rsv":     "but his delight is in the law of the LORD, and on his law he meditates day and night."
      },
      {
        "verse": 3,
        "hebrew":  "וְהָיָה כְּעֵץ שָׁתוּל עַל פַּלְגֵי מָיִם אֲשֶׁר פִּרְיוֹ יִתֵּן בְּעִתּוֹ וְעָלֵהוּ לֹא יִבּוֹל וְכֹל אֲשֶׁר יַעֲשֶׂה יַצְלִיחַ׃",
        "latin":   "Et erit tamquam lignum, quod plantatum est secus decursus aquarum, quod fructum suum dabit in tempore suo; et folium ejus non defluet; et omnia, quaecumque faciet, prosperabuntur.",
        "kjv":     "And he shall be like a tree planted by the rivers of water, that bringeth forth his fruit in his season; his leaf also shall not wither; and whatsoever he doeth shall prosper.",
        "esv":     "He is like a tree planted by streams of water that yields its fruit in its season, and its leaf does not wither. In all that he does, he prospers.",
        "rsv":     "He is like a tree planted by streams of water, that yields its fruit in its season, and its leaf does not wither. In all that he does, he prospers."
      },
      {
        "verse": 4,
        "hebrew":  "לֹא כֵן הָרְשָׁעִים כִּי אִם כַּמֹּץ אֲשֶׁר תִּדְּפֶנּוּ רוּחַ׃",
        "latin":   "Non sic impii, non sic; sed tamquam pulvis, quem projicit ventus a facie terrae.",
        "kjv":     "The ungodly are not so: but are like the chaff which the wind driveth away.",
        "esv":     "The wicked are not so, but are like chaff that the wind drives away.",
        "rsv":     "The wicked are not so, but are like chaff which the wind drives away."
      },
      {
        "verse": 5,
        "hebrew":  "עַל כֵּן לֹא יָקֻמוּ רְשָׁעִים בַּמִּשְׁפָּט וְחַטָּאִים בַּעֲדַת צַדִּיקִים׃",
        "latin":   "Ideo non resurgent impii in judicio, neque peccatores in concilio justorum.",
        "kjv":     "Therefore the ungodly shall not stand in the judgment, nor sinners in the congregation of the righteous.",
        "esv":     "Therefore the wicked will not stand in the judgment, nor sinners in the congregation of the righteous;",
        "rsv":     "Therefore the wicked will not stand in the judgment, nor sinners in the congregation of the righteous;"
      },
      {
        "verse": 6,
        "hebrew":  "כִּי יוֹדֵעַ יְהוָה דֶּרֶךְ צַדִּיקִים וְדֶרֶךְ רְשָׁעִים תֹּאבֵד׃",
        "latin":   "Quoniam novit Dominus viam justorum; et iter impiorum peribit.",
        "kjv":     "For the LORD knoweth the way of the righteous: but the way of the ungodly shall perish.",
        "esv":     "for the LORD knows the way of the righteous, but the way of the wicked will perish.",
        "rsv":     "for the LORD knows the way of the righteous, but the way of the wicked will perish."
      }
    ]
  },
  {
    "psalm": 22,
    "title": "Psalm 22",
    "superscript": "My God, My God — A Cry of Desolation and Praise",
    "verses": [
      {
        "verse": 1,
        "hebrew":  "לַמְנַצֵּחַ עַל אַיֶּלֶת הַשַּׁחַר מִזְמוֹר לְדָוִד׃",
        "latin":   "In finem, pro susceptione matutina. Psalmus David.",
        "kjv":     "[To the chief Musician upon Aijeleth Shahar, A Psalm of David.]",
        "esv":     "[To the choirmaster: according to The Doe of the Dawn. A Psalm of David.]",
        "rsv":     "[To the choirmaster: according to The Hind of the Dawn. A Psalm of David.]"
      },
      {
        "verse": 2,
        "hebrew":  "אֵלִי אֵלִי לָמָה עֲזַבְתָּנִי רָחוֹק מִישׁוּעָתִי דִּבְרֵי שַׁאֲגָתִי׃",
        "latin":   "Deus, Deus meus, respice in me: quare me dereliquisti? longe a salute mea verba delictorum meorum.",
        "kjv":     "My God, my God, why hast thou forsaken me? why art thou so far from helping me, and from the words of my roaring?",
        "esv":     "My God, my God, why have you forsaken me? Why are you so far from saving me, from the words of my groaning?",
        "rsv":     "My God, my God, why hast thou forsaken me? Why art thou so far from helping me, from the words of my groaning?"
      },
      {
        "verse": 3,
        "hebrew":  "אֱלֹהַי אֶקְרָא יוֹמָם וְלֹא תַעֲנֶה וְלַיְלָה וְלֹא דוּמִיָּה לִי׃",
        "latin":   "Deus meus, clamabo per diem, et non exaudies; et nocte, et non ad insipientiam mihi.",
        "kjv":     "O my God, I cry in the daytime, but thou hearest not; and in the night season, and am not silent.",
        "esv":     "O my God, I cry by day, but you do not answer, and by night, but I find no rest.",
        "rsv":     "O my God, I cry by day, but thou dost not answer; and by night, but find no rest."
      },
      {
        "verse": 4,
        "hebrew":  "וְאַתָּה קָדוֹשׁ יוֹשֵׁב תְּהִלּוֹת יִשְׂרָאֵל׃",
        "latin":   "Tu autem in sancto habitas, laus Israel.",
        "kjv":     "But thou art holy, O thou that inhabitest the praises of Israel.",
        "esv":     "Yet you are holy, enthroned on the praises of Israel.",
        "rsv":     "Yet thou art holy, enthroned on the praises of Israel."
      },
      {
        "verse": 5,
        "hebrew":  "בְּךָ בָּטְחוּ אֲבֹתֵינוּ בָּטְחוּ וַתְּפַלְּטֵמוֹ׃",
        "latin":   "In te speraverunt patres nostri: speraverunt, et liberasti eos.",
        "kjv":     "Our fathers trusted in thee: they trusted, and thou didst deliver them.",
        "esv":     "In you our fathers trusted; they trusted, and you delivered them.",
        "rsv":     "In thee our fathers trusted; they trusted, and thou didst deliver them."
      },
      {
        "verse": 6,
        "hebrew":  "אֵלֶיךָ זָעֲקוּ וְנִמְלָטוּ בְּךָ בָטְחוּ וְלֹא בוֹשׁוּ׃",
        "latin":   "Ad te clamaverunt, et salvi facti sunt; in te speraverunt, et non sunt confusi.",
        "kjv":     "They cried unto thee, and were delivered: they trusted in thee, and were not confounded.",
        "esv":     "To you they cried and were rescued; in you they trusted and were not put to shame.",
        "rsv":     "To thee they cried, and were saved; in thee they trusted, and were not disappointed."
      },
      {
        "verse": 7,
        "hebrew":  "וְאָנֹכִי תוֹלַעַת וְלֹא אִישׁ חֶרְפַּת אָדָם וּבְזוּי עָם׃",
        "latin":   "Ego autem sum vermis, et non homo; opprobrium hominum, et abjectio plebis.",
        "kjv":     "But I am a worm, and no man; a reproach of men, and despised of the people.",
        "esv":     "But I am a worm and not a man, scorned by mankind and despised by the people.",
        "rsv":     "But I am a worm, and no man; scorned by men, and despised by the people."
      },
      {
        "verse": 8,
        "hebrew":  "כָּל רֹאַי יַלְעִגוּ לִי יַפְטִירוּ בְשָׂפָה יָנִיעוּ רֹאשׁ׃",
        "latin":   "Omnes videntes me, deriserunt me; locuti sunt labiis, et moverunt caput.",
        "kjv":     "All they that see me laugh me to scorn: they shoot out the lip, they shake the head,",
        "esv":     "All who see me mock me; they make mouths at me; they wag their heads;",
        "rsv":     "All who see me mock at me, they make mouths at me, they wag their heads;"
      },
      {
        "verse": 9,
        "hebrew":  "גֹּל אֶל יְהוָה יְפַלְּטֵהוּ יַצִּילֵהוּ כִּי חָפֵץ בוֹ׃",
        "latin":   "Speravit in Domino, eripiat eum; salvum faciat eum, quoniam vult eum.",
        "kjv":     "He trusted on the LORD that he would deliver him: let him deliver him, seeing he delighted in him.",
        "esv":     "\"He trusts in the LORD; let him deliver him; let him rescue him, for he delights in him!\"",
        "rsv":     "\"He committed his cause to the LORD; let him deliver him, let him rescue him, for he delights in him!\""
      },
      {
        "verse": 10,
        "hebrew":  "כִּי אַתָּה גֹחִי מִבָּטֶן מַבְטִיחִי עַל שְׁדֵי אִמִּי׃",
        "latin":   "Quoniam tu es, qui extraxisti me de ventre; spes mea ab uberibus matris meae.",
        "kjv":     "But thou art he that took me out of the womb: thou didst make me hope when I was upon my mother's breasts.",
        "esv":     "Yet you are he who took me from the womb; you made me trust you at my mother's breasts.",
        "rsv":     "Yet thou art he who took me from the womb; thou didst keep me safe upon my mother's breasts."
      },
      {
        "verse": 11,
        "hebrew":  "עָלֶיךָ הָשְׁלַכְתִּי מֵרָחֶם מִבֶּטֶן אִמִּי אֵלִי אָתָּה׃",
        "latin":   "In te projectus sum ex utero; de ventre matris meae Deus meus es tu.",
        "kjv":     "I was cast upon thee from the womb: thou art my God from my mother's belly.",
        "esv":     "On you was I cast from my birth, and from my mother's womb you have been my God.",
        "rsv":     "Upon thee was I cast from my birth, and since my mother bore me thou hast been my God."
      },
      {
        "verse": 12,
        "hebrew":  "אַל תִּרְחַק מִמֶּנִּי כִּי צָרָה קְרוֹבָה כִּי אֵין עוֹזֵר׃",
        "latin":   "Ne discesseris a me; quoniam tribulatio proxima est, quoniam non est qui adjuvet.",
        "kjv":     "Be not far from me; for trouble is near; for there is none to help.",
        "esv":     "Be not far from me, for trouble is near, and there is none to help.",
        "rsv":     "Be not far from me, for trouble is near and there is none to help."
      },
      {
        "verse": 13,
        "hebrew":  "סְבָבוּנִי פָּרִים רַבִּים אַבִּירֵי בָשָׁן כִּתְּרוּנִי׃",
        "latin":   "Circumdederunt me vituli multi; tauri pingues obsederunt me.",
        "kjv":     "Many bulls have compassed me: strong bulls of Bashan have beset me round.",
        "esv":     "Many bulls encompass me; strong bulls of Bashan surround me;",
        "rsv":     "Many bulls encompass me, strong bulls of Bashan surround me;"
      },
      {
        "verse": 14,
        "hebrew":  "פָּצוּ עָלַי פִּיהֶם אַרְיֵה טֹרֵף וְשֹׁאֵג׃",
        "latin":   "Aperuerunt super me os suum, sicut leo rapiens et rugiens.",
        "kjv":     "They gaped upon me with their mouths, as a ravening and a roaring lion.",
        "esv":     "they open wide their mouths at me, like a ravening and roaring lion.",
        "rsv":     "they open wide their mouths at me, like a ravening and roaring lion."
      },
      {
        "verse": 15,
        "hebrew":  "כַּמַּיִם נִשְׁפַּכְתִּי וְהִתְפָּרְדוּ כָּל עַצְמוֹתָי הָיָה לִבִּי כַּדּוֹנָג נָמֵס בְּתוֹךְ מֵעָי׃",
        "latin":   "Sicut aqua effusus sum; et dispersa sunt omnia ossa mea. Factum est cor meum tamquam cera liquescens in medio ventris mei.",
        "kjv":     "I am poured out like water, and all my bones are out of joint: my heart is like wax; it is melted in the midst of my bowels.",
        "esv":     "I am poured out like water, and all my bones are out of joint; my heart is like wax; it is melted within my breast;",
        "rsv":     "I am poured out like water, and all my bones are out of joint; my heart is like wax, it is melted within my breast;"
      },
      {
        "verse": 16,
        "hebrew":  "יָבֵשׁ כַּחֶרֶשׂ כֹּחִי וּלְשׁוֹנִי מֻדְבָּק מַלְקוֹחָי וְלַעֲפַר מָוֶת תִּשְׁפְּתֵנִי׃",
        "latin":   "Aruit tamquam testa virtus mea, et lingua mea adhaesit faucibus meis; et in pulverem mortis deduxisti me.",
        "kjv":     "My strength is dried up like a potsherd; and my tongue cleaveth to my jaws; and thou hast brought me into the dust of death.",
        "esv":     "my strength is dried up like a potsherd; and my tongue sticks to my jaws; you lay me in the dust of death.",
        "rsv":     "my strength is dried up like a potsherd; and my tongue cleaves to my jaws; thou dost lay me in the dust of death."
      },
      {
        "verse": 17,
        "hebrew":  "כִּי סְבָבוּנִי כְּלָבִים עֲדַת מְרֵעִים הִקִּיפוּנִי כָּאֲרִי יָדַי וְרַגְלָי׃",
        "latin":   "Quoniam circumdederunt me canes multi; concilium malignantium obsedit me. Foderunt manus meas et pedes meos;",
        "kjv":     "For dogs have compassed me: the assembly of the wicked have inclosed me: they pierced my hands and my feet.",
        "esv":     "For dogs encompass me; a company of evildoers encircles me; they have pierced my hands and feet—",
        "rsv":     "Yea, dogs are round about me; a company of evildoers encircle me; they have pierced my hands and feet—"
      },
      {
        "verse": 18,
        "hebrew":  "אֲסַפֵּר כָּל עַצְמוֹתָי הֵמָּה יַבִּיטוּ יִרְאוּ בִי׃",
        "latin":   "dinumeraverunt omnia ossa mea. Ipsi vero consideraverunt et inspexerunt me.",
        "kjv":     "I may tell all my bones: they look and stare upon me.",
        "esv":     "I can count all my bones— they stare and gloat over me;",
        "rsv":     "I can count all my bones— they stare and gloat over me;"
      },
      {
        "verse": 19,
        "hebrew":  "יְחַלְּקוּ בְגָדַי לָהֶם וְעַל לְבוּשִׁי יַפִּילוּ גוֹרָל׃",
        "latin":   "Diviserunt sibi vestimenta mea, et super vestem meam miserunt sortem.",
        "kjv":     "They part my garments among them, and cast lots upon my vesture.",
        "esv":     "they divide my garments among them, and for my clothing they cast lots.",
        "rsv":     "they divide my garments among them, and for my raiment they cast lots."
      },
      {
        "verse": 20,
        "hebrew":  "וְאַתָּה יְהוָה אַל תִּרְחָק אֱיָלוּתִי לְעֶזְרָתִי חוּשָׁה׃",
        "latin":   "Tu autem, Domine, ne elongaveris auxilium tuum a me; ad defensionem meam conspice.",
        "kjv":     "But be not thou far from me, O LORD: O my strength, haste thee to help me.",
        "esv":     "But you, O LORD, do not be far off! O you my help, come quickly to my aid!",
        "rsv":     "But thou, O LORD, be not far off! O thou my help, hasten to my aid!"
      },
      {
        "verse": 21,
        "hebrew":  "הַצִּילָה מֵחֶרֶב נַפְשִׁי מִיַּד כֶּלֶב יְחִידָתִי׃",
        "latin":   "Erue a framea, Deus, animam meam; et de manu canis unicam meam.",
        "kjv":     "Deliver my soul from the sword; my darling from the power of the dog.",
        "esv":     "Deliver my soul from the sword, my precious life from the power of the dog!",
        "rsv":     "Deliver my soul from the sword, my life from the power of the dog!"
      },
      {
        "verse": 22,
        "hebrew":  "הוֹשִׁיעֵנִי מִפִּי אַרְיֵה וּמִקַּרְנֵי רֵמִים עֲנִיתָנִי׃",
        "latin":   "Salva me ex ore leonis; et a cornibus unicornium humilitatem meam.",
        "kjv":     "Save me from the lion's mouth: for thou hast heard me from the horns of the unicorns.",
        "esv":     "Save me from the mouth of the lion! You have rescued me from the horns of the wild oxen!",
        "rsv":     "Save me from the mouth of the lion, my afflicted soul from the horns of the wild oxen!"
      },
      {
        "verse": 23,
        "hebrew":  "אֲסַפְּרָה שִׁמְךָ לְאֶחָי בְּתוֹךְ קָהָל אֲהַלְלֶךָּ׃",
        "latin":   "Narrabo nomen tuum fratribus meis; in medio ecclesiae laudabo te.",
        "kjv":     "I will declare thy name unto my brethren: in the midst of the congregation will I praise thee.",
        "esv":     "I will tell of your name to my brothers; in the midst of the congregation I will praise you:",
        "rsv":     "I will tell of thy name to my brethren; in the midst of the congregation I will praise thee:"
      },
      {
        "verse": 24,
        "hebrew":  "יִרְאֵי יְהוָה הַלְלוּהוּ כָּל זֶרַע יַעֲקֹב כַּבְּדוּהוּ וְגוּרוּ מִמֶּנּוּ כָּל זֶרַע יִשְׂרָאֵל׃",
        "latin":   "Qui timetis Dominum, laudate eum; universum semen Jacob, glorificate eum.",
        "kjv":     "Ye that fear the LORD, praise him; all ye the seed of Jacob, glorify him; and fear him, all ye the seed of Israel.",
        "esv":     "You who fear the LORD, praise him! All you offspring of Jacob, glorify him, and stand in awe of him, all you offspring of Israel!",
        "rsv":     "You who fear the LORD, praise him! all you sons of Jacob, glorify him, and stand in awe of him, all you sons of Israel!"
      },
      {
        "verse": 25,
        "hebrew":  "כִּי לֹא בָזָה וְלֹא שִׁקַּץ עֱנוּת עָנִי וְלֹא הִסְתִּיר פָּנָיו מִמֶּנּוּ וּבְשַׁוְּעוֹ אֵלָיו שָׁמֵעַ׃",
        "latin":   "Quoniam non sprevit, neque despexit deprecationem pauperis; nec avertit faciem suam a me; et cum clamaret ad eum, exaudivit eum.",
        "kjv":     "For he hath not despised nor abhorred the affliction of the afflicted; neither hath he hidden his face from him; but when he cried unto him, he heard.",
        "esv":     "For he has not despised or scorned the suffering of the afflicted one; he has not hidden his face from him but has listened to his cry for help.",
        "rsv":     "For he has not despised or abhorred the affliction of the afflicted; and he has not hid his face from him, but has heard, when he cried to him."
      },
      {
        "verse": 26,
        "hebrew":  "מֵאִתְּךָ תְהִלָּתִי בְּקָהָל רָב נְדָרַי אֲשַׁלֵּם נֶגֶד יְרֵאָיו׃",
        "latin":   "Apud te laus mea in ecclesia magna; vota mea reddam in conspectu timentium eum.",
        "kjv":     "My praise shall be of thee in the great congregation: I will pay my vows before them that fear him.",
        "esv":     "From you comes my praise in the great congregation; my vows I will perform before those who fear him.",
        "rsv":     "From thee comes my praise in the great congregation; my vows I will pay before those who fear him."
      },
      {
        "verse": 27,
        "hebrew":  "יֹאכְלוּ עֲנָוִים וְיִשְׂבָּעוּ יְהַלְלוּ יְהוָה דֹּרְשָׁיו יְחִי לְבַבְכֶם לָעַד׃",
        "latin":   "Edent pauperes, et saturabuntur; et laudabunt Dominum, qui requirunt eum; vivent corda eorum in saeculum saeculi.",
        "kjv":     "The meek shall eat and be satisfied: they shall praise the LORD that seek him: your heart shall live for ever.",
        "esv":     "The afflicted shall eat and be satisfied; those who seek him shall praise the LORD! May your hearts live forever!",
        "rsv":     "The afflicted shall eat and be satisfied; those who seek him shall praise the LORD! May your hearts live for ever!"
      },
      {
        "verse": 28,
        "hebrew":  "יִזְכְּרוּ וְיָשֻׁבוּ אֶל יְהוָה כָּל אַפְסֵי אָרֶץ וְיִשְׁתַּחֲווּ לְפָנֶיךָ כָּל מִשְׁפְּחוֹת גּוֹיִם׃",
        "latin":   "Reminiscentur, et convertentur ad Dominum universi fines terrae; et adorabunt in conspectu ejus universae familiae gentium.",
        "kjv":     "All the ends of the world shall remember and turn unto the LORD: and all the kindreds of the nations shall worship before thee.",
        "esv":     "All the ends of the earth shall remember and turn to the LORD, and all the families of the nations shall worship before you.",
        "rsv":     "All the ends of the earth shall remember and turn to the LORD; and all the families of the nations shall worship before him."
      },
      {
        "verse": 29,
        "hebrew":  "כִּי לַיהוָה הַמְּלוּכָה וּמֹשֵׁל בַּגּוֹיִם׃",
        "latin":   "Quoniam Domini est regnum; et ipse dominabitur gentium.",
        "kjv":     "For the kingdom is the LORD's: and he is the governor among the nations.",
        "esv":     "For kingship belongs to the LORD, and he rules over the nations.",
        "rsv":     "For dominion belongs to the LORD, and he rules over the nations."
      },
      {
        "verse": 30,
        "hebrew":  "אָכְלוּ וַיִּשְׁתַּחֲווּ כָּל דִּשְׁנֵי אֶרֶץ לְפָנָיו יִכְרְעוּ כָּל יוֹרְדֵי עָפָר וְנַפְשׁוֹ לֹא חִיָּה׃",
        "latin":   "Manducaverunt et adoraverunt omnes pingues terrae; in conspectu ejus cadent omnes qui descendunt in terram.",
        "kjv":     "All they that be fat upon earth shall eat and worship: all they that go down to the dust shall bow before him: and none can keep alive his own soul.",
        "esv":     "All the prosperous of the earth eat and worship; before him shall bow all who go down to the dust, even the one who could not keep himself alive.",
        "rsv":     "Yea, to him shall all the proud of the earth bow down; before him shall bow all who go down to the dust, and he who cannot keep himself alive."
      },
      {
        "verse": 31,
        "hebrew":  "זֶרַע יַעַבְדֶנּוּ יְסֻפַּר לַאדֹנָי לַדּוֹר׃",
        "latin":   "Et semen meum serviet ipsi; annuntiabitur Domino generatio ventura.",
        "kjv":     "A seed shall serve him; it shall be accounted to the Lord for a generation.",
        "esv":     "Posterity shall serve him; it shall be told of the Lord to the coming generation;",
        "rsv":     "Posterity shall serve him; men shall tell of the Lord to the coming generation,"
      },
      {
        "verse": 32,
        "hebrew":  "יָבֹאוּ וְיַגִּידוּ צִדְקָתוֹ לְעַם נוֹלָד כִּי עָשָׂה׃",
        "latin":   "Et annuntiabunt justitiam ejus populo qui nascetur, quem fecit Dominus.",
        "kjv":     "They shall come, and shall declare his righteousness unto a people that shall be born, that he hath done this.",
        "esv":     "they shall come and proclaim his righteousness to a people yet unborn, that he has done it.",
        "rsv":     "and proclaim his deliverance to a people yet unborn, that he has wrought it."
      }
    ]
  },
  {
    "psalm": 23,
    "title": "Psalm 23",
    "superscript": "The Lord is My Shepherd",
    "verses": [
      {
        "verse": 1,
        "hebrew":  "מִזְמוֹר לְדָוִד יְהוָה רֹעִי לֹא אֶחְסָר׃",
        "latin":   "Psalmus David. Dominus regit me, et nihil mihi deerit:",
        "kjv":     "The LORD is my shepherd; I shall not want.",
        "esv":     "The LORD is my shepherd; I shall not want.",
        "rsv":     "The LORD is my shepherd, I shall not want;"
      },
      {
        "verse": 2,
        "hebrew":  "בִּנְאוֹת דֶּשֶׁא יַרְבִּיצֵנִי עַל מֵי מְנֻחוֹת יְנַהֲלֵנִי׃",
        "latin":   "in loco pascuae ibi me collocavit. Super aquam refectionis educavit me;",
        "kjv":     "He maketh me to lie down in green pastures: he leadeth me beside the still waters.",
        "esv":     "He makes me lie down in green pastures. He leads me beside still waters.",
        "rsv":     "he makes me lie down in green pastures. He leads me beside still waters;"
      },
      {
        "verse": 3,
        "hebrew":  "נַפְשִׁי יְשׁוֹבֵב יַנְחֵנִי בְמַעְגְּלֵי צֶדֶק לְמַעַן שְׁמוֹ׃",
        "latin":   "animam meam convertit. Deduxit me super semitas justitiae, propter nomen suum.",
        "kjv":     "He restoreth my soul: he leadeth me in the paths of righteousness for his name's sake.",
        "esv":     "He restores my soul. He leads me in paths of righteousness for his name's sake.",
        "rsv":     "he restores my soul. He leads me in paths of righteousness for his name's sake."
      },
      {
        "verse": 4,
        "hebrew":  "גַּם כִּי אֵלֵךְ בְּגֵיא צַלְמָוֶת לֹא אִירָא רָע כִּי אַתָּה עִמָּדִי שִׁבְטְךָ וּמִשְׁעַנְתֶּךָ הֵמָּה יְנַחֲמֻנִי׃",
        "latin":   "Nam etsi ambulavero in medio umbrae mortis, non timebo mala, quoniam tu mecum es. Virga tua et baculus tuus, ipsa me consolata sunt.",
        "kjv":     "Yea, though I walk through the valley of the shadow of death, I will fear no evil: for thou art with me; thy rod and thy staff they comfort me.",
        "esv":     "Even though I walk through the valley of the shadow of death, I will fear no evil, for you are with me; your rod and your staff, they comfort me.",
        "rsv":     "Even though I walk through the valley of the shadow of death, I fear no evil; for thou art with me; thy rod and thy staff, they comfort me."
      },
      {
        "verse": 5,
        "hebrew":  "תַּעֲרֹךְ לְפָנַי שֻׁלְחָן נֶגֶד צֹרְרָי דִּשַּׁנְתָּ בַשֶּׁמֶן רֹאשִׁי כּוֹסִי רְוָיָה׃",
        "latin":   "Parasti in conspectu meo mensam, adversus eos qui tribulant me. Impinguasti in oleo caput meum; et calix meus inebrians quam praeclarus est!",
        "kjv":     "Thou preparest a table before me in the presence of mine enemies: thou anointest my head with oil; my cup runneth over.",
        "esv":     "You prepare a table before me in the presence of my enemies; you anoint my head with oil; my cup overflows.",
        "rsv":     "Thou preparest a table before me in the presence of my enemies; thou anointest my head with oil, my cup overflows."
      },
      {
        "verse": 6,
        "hebrew":  "אַךְ טוֹב וָחֶסֶד יִרְדְּפוּנִי כָּל יְמֵי חַיַּי וְשַׁבְתִּי בְּבֵית יְהוָה לְאֹרֶךְ יָמִים׃",
        "latin":   "Et misericordia tua subsequetur me omnibus diebus vitae meae; et ut inhabitem in domo Domini, in longitudinem dierum.",
        "kjv":     "Surely goodness and mercy shall follow me all the days of my life: and I will dwell in the house of the LORD for ever.",
        "esv":     "Surely goodness and mercy shall follow me all the days of my life, and I shall dwell in the house of the LORD forever.",
        "rsv":     "Surely goodness and mercy shall follow me all the days of my life; and I shall dwell in the house of the LORD for ever."
      }
    ]
  },
  {
    "psalm": 51,
    "title": "Psalm 51",
    "superscript": "Miserere — Prayer of Repentance",
    "verses": [
      { "verse": 1, "hebrew": "לַמְנַצֵּחַ מִזְמוֹר לְדָוִד׃", "latin": "In finem. Psalmus David,", "kjv": "[To the chief Musician, A Psalm of David, when Nathan the prophet came unto him, after he had gone in to Bath-sheba.]", "esv": "[To the choirmaster. A Psalm of David, when Nathan the prophet went to him, after he had gone in to Bathsheba.]", "rsv": "[To the choirmaster. A Psalm of David, when Nathan the prophet came to him, after he had gone in to Bathsheba.]" },
      { "verse": 2, "hebrew": "בְּבוֹא אֵלָיו נָתָן הַנָּבִיא כַּאֲשֶׁר בָּא אֶל בַּת שָׁבַע׃", "latin": "cum venit ad eum Nathan propheta, quando intravit ad Bethsabee.", "kjv": "Have mercy upon me, O God, according to thy lovingkindness: according unto the multitude of thy tender mercies blot out my transgressions.", "esv": "Have mercy on me, O God, according to your steadfast love; according to your abundant mercy blot out my transgressions.", "rsv": "Have mercy on me, O God, according to thy steadfast love; according to thy abundant mercy blot out my transgressions." },
      { "verse": 3, "hebrew": "חָנֵּנִי אֱלֹהִים כְּחַסְדֶּךָ כְּרֹב רַחֲמֶיךָ מְחֵה פְשָׁעָי׃", "latin": "Miserere mei, Deus, secundum magnam misericordiam tuam; et secundum multitudinem miserationum tuarum, dele iniquitatem meam.", "kjv": "Have mercy upon me, O God, according to thy lovingkindness: according unto the multitude of thy tender mercies blot out my transgressions.", "esv": "Have mercy on me, O God, according to your steadfast love; according to your abundant mercy blot out my transgressions.", "rsv": "Have mercy on me, O God, according to thy steadfast love; according to thy abundant mercy blot out my transgressions." },
      { "verse": 4, "hebrew": "הֶרֶב כַּבְּסֵנִי מֵעֲוֹנִי וּמֵחַטָּאתִי טַהֲרֵנִי׃", "latin": "Amplius lava me ab iniquitate mea, et a peccato meo munda me.", "kjv": "Wash me throughly from mine iniquity, and cleanse me from my sin.", "esv": "Wash me thoroughly from my iniquity, and cleanse me from my sin!", "rsv": "Wash me thoroughly from my iniquity, and cleanse me from my sin!" },
      { "verse": 5, "hebrew": "כִּי פְשָׁעַי אֲנִי אֵדָע וְחַטָּאתִי נֶגְדִּי תָמִיד׃", "latin": "Quoniam iniquitatem meam ego cognosco; et peccatum meum contra me est semper.", "kjv": "For I acknowledge my transgressions: and my sin is ever before me.", "esv": "For I know my transgressions, and my sin is ever before me.", "rsv": "For I know my transgressions, and my sin is ever before me." },
      { "verse": 6, "hebrew": "לְךָ לְבַדְּךָ חָטָאתִי וְהָרַע בְּעֵינֶיךָ עָשִׂיתִי לְמַעַן תִּצְדַּק בְּדָבְרֶךָ תִּזְכֶּה בְשָׁפְטֶךָ׃", "latin": "Tibi soli peccavi, et malum coram te feci; ut justificeris in sermonibus tuis, et vincas cum judicaris.", "kjv": "Against thee, thee only, have I sinned, and done this evil in thy sight: that thou mightest be justified when thou speakest, and be clear when thou judgest.", "esv": "Against you, you only, have I sinned and done what is evil in your sight, so that you may be justified in your words and blameless in your judgment.", "rsv": "Against thee, thee only, have I sinned, and done that which is evil in thy sight, so that thou art justified in thy sentence and blameless in thy judgment." },
      { "verse": 7, "hebrew": "הֵן בְּעָווֹן חוֹלָלְתִּי וּבְחֵטְא יֶחֱמַתְנִי אִמִּי׃", "latin": "Ecce enim in iniquitatibus conceptus sum; et in peccatis concepit me mater mea.", "kjv": "Behold, I was shapen in iniquity; and in sin did my mother conceive me.", "esv": "Behold, I was brought forth in iniquity, and in sin did my mother conceive me.", "rsv": "Behold, I was brought forth in iniquity, and in sin did my mother conceive me." },
      { "verse": 8, "hebrew": "הֵן אֱמֶת חָפַצְתָּ בַטֻּחוֹת וּבְסָתֻם חָכְמָה תוֹדִיעֵנִי׃", "latin": "Ecce enim veritatem dilexisti; incerta et occulta sapientiae tuae manifestasti mihi.", "kjv": "Behold, thou desirest truth in the inward parts: and in the hidden part thou shalt make me to know wisdom.", "esv": "Behold, you delight in truth in the inward being, and you teach me wisdom in the secret heart.", "rsv": "Behold, thou desirest truth in the inward being; therefore teach me wisdom in my secret heart." },
      { "verse": 9, "hebrew": "תְּחַטְּאֵנִי בְאֵזוֹב וְאֶטְהָר תְּכַבְּסֵנִי וּמִשֶּׁלֶג אַלְבִּין׃", "latin": "Asperges me hyssopo, et mundabor; lavabis me, et super nivem dealbabor.", "kjv": "Purge me with hyssop, and I shall be clean: wash me, and I shall be whiter than snow.", "esv": "Purge me with hyssop, and I shall be clean; wash me, and I shall be whiter than snow.", "rsv": "Purge me with hyssop, and I shall be clean; wash me, and I shall be whiter than snow." },
      { "verse": 10, "hebrew": "תַּשְׁמִיעֵנִי שָׂשׂוֹן וְשִׂמְחָה תָּגֵלְנָה עֲצָמוֹת דִּכִּיתָ׃", "latin": "Auditui meo dabis gaudium et laetitiam; et exsultabunt ossa humiliata.", "kjv": "Make me to hear joy and gladness; that the bones which thou hast broken may rejoice.", "esv": "Let me hear joy and gladness; let the bones that you have broken rejoice.", "rsv": "Fill me with joy and gladness; let the bones which thou hast broken rejoice." },
      { "verse": 11, "hebrew": "הַסְתֵּר פָּנֶיךָ מֵחֲטָאָי וְכָל עֲוֹנֹתַי מְחֵה׃", "latin": "Averte faciem tuam a peccatis meis; et omnes iniquitates meas dele.", "kjv": "Hide thy face from my sins, and blot out all mine iniquities.", "esv": "Hide your face from my sins, and blot out all my iniquities.", "rsv": "Hide thy face from my sins, and blot out all my iniquities." },
      { "verse": 12, "hebrew": "לֵב טָהוֹר בְּרָא לִי אֱלֹהִים וְרוּחַ נָכוֹן חַדֵּשׁ בְּקִרְבִּי׃", "latin": "Cor mundum crea in me, Deus; et spiritum rectum innova in visceribus meis.", "kjv": "Create in me a clean heart, O God; and renew a right spirit within me.", "esv": "Create in me a clean heart, O God, and renew a right spirit within me.", "rsv": "Create in me a clean heart, O God, and put a new and right spirit within me." },
      { "verse": 13, "hebrew": "אַל תַּשְׁלִיכֵנִי מִלְּפָנֶיךָ וְרוּחַ קָדְשְׁךָ אַל תִּקַּח מִמֶּנִּי׃", "latin": "Ne projicias me a facie tua; et spiritum sanctum tuum ne auferas a me.", "kjv": "Cast me not away from thy presence; and take not thy holy spirit from me.", "esv": "Cast me not away from your presence, and take not your Holy Spirit from me.", "rsv": "Cast me not away from thy presence, and take not thy holy Spirit from me." },
      { "verse": 14, "hebrew": "הָשִׁיבָה לִּי שְׂשׂוֹן יִשְׁעֶךָ וְרוּחַ נְדִיבָה תִסְמְכֵנִי׃", "latin": "Redde mihi laetitiam salutaris tui; et spiritu principali confirma me.", "kjv": "Restore unto me the joy of thy salvation; and uphold me with thy free spirit.", "esv": "Restore to me the joy of your salvation, and uphold me with a willing spirit.", "rsv": "Restore to me the joy of thy salvation, and uphold me with a willing spirit." },
      { "verse": 15, "hebrew": "אֲלַמְּדָה פֹשְׁעִים דְּרָכֶיךָ וְחַטָּאִים אֵלֶיךָ יָשׁוּבוּ׃", "latin": "Docebo iniquos vias tuas; et impii ad te convertentur.", "kjv": "Then will I teach transgressors thy ways; and sinners shall be converted unto thee.", "esv": "Then I will teach transgressors your ways, and sinners will return to you.", "rsv": "Then I will teach transgressors your ways, and sinners will return to thee." },
      { "verse": 16, "hebrew": "הַצִּילֵנִי מִדָּמִים אֱלֹהִים אֱלֹהֵי תְּשׁוּעָתִי תְּרַנֵּן לְשׁוֹנִי צִדְקָתֶךָ׃", "latin": "Libera me de sanguinibus, Deus, Deus salutis meae; et exsultabit lingua mea justitiam tuam.", "kjv": "Deliver me from bloodguiltiness, O God, thou God of my salvation: and my tongue shall sing aloud of thy righteousness.", "esv": "Deliver me from bloodguiltiness, O God, O God of my salvation, and my tongue will sing aloud of your righteousness.", "rsv": "Deliver me from bloodguiltiness, O God, thou God of my salvation, and my tongue will sing aloud of thy deliverance." },
      { "verse": 17, "hebrew": "אֲדֹנָי שְׂפָתַי תִּפְתָּח וּפִי יַגִּיד תְּהִלָּתֶךָ׃", "latin": "Domine, labia mea aperies; et os meum annuntiabit laudem tuam.", "kjv": "O Lord, open thou my lips; and my mouth shall shew forth thy praise.", "esv": "O Lord, open my lips, and my mouth will declare your praise.", "rsv": "O Lord, open thou my lips, and my mouth shall show forth thy praise." },
      { "verse": 18, "hebrew": "כִּי לֹא תַחְפֹּץ זֶבַח וְאֶתֵּנָה עוֹלָה לֹא תִרְצֶה׃", "latin": "Quoniam si voluisses sacrificium, dedissem utique; holocaustis non delectaberis.", "kjv": "For thou desirest not sacrifice; else would I give it: thou delightest not in burnt offering.", "esv": "For you will not delight in sacrifice, or I would give it; you will not be pleased with a burnt offering.", "rsv": "For thou hast no delight in sacrifice; were I to give a burnt offering, thou wouldst not be pleased." },
      { "verse": 19, "hebrew": "זִבְחֵי אֱלֹהִים רוּחַ נִשְׁבָּרָה לֵב נִשְׁבָּר וְנִדְכֶּה אֱלֹהִים לֹא תִבְזֶה׃", "latin": "Sacrificium Deo spiritus contribulatus; cor contritum et humiliatum, Deus, non despicies.", "kjv": "The sacrifices of God are a broken spirit: a broken and a contrite heart, O God, thou wilt not despise.", "esv": "The sacrifices of God are a broken spirit; a broken and contrite heart, O God, you will not despise.", "rsv": "The sacrifice acceptable to God is a broken spirit; a broken and contrite heart, O God, thou wilt not despise." },
      { "verse": 20, "hebrew": "הֵיטִיבָה בִרְצוֹנְךָ אֶת צִיּוֹן תִּבְנֶה חוֹמוֹת יְרוּשָׁלָם׃", "latin": "Benigne fac, Domine, in bona voluntate tua Sion, ut aedificentur muri Hierusalem.", "kjv": "Do good in thy good pleasure unto Zion: build thou the walls of Jerusalem.", "esv": "Do good to Zion in your good pleasure; build up the walls of Jerusalem;", "rsv": "Do good to Zion in thy good pleasure; rebuild the walls of Jerusalem," },
      { "verse": 21, "hebrew": "אָז תַּחְפֹּץ זִבְחֵי צֶדֶק עוֹלָה וְכָלִיל אָז יַעֲלוּ עַל מִזְבַּחֲךָ פָרִים׃", "latin": "Tunc acceptabis sacrificium justitiae, oblationes et holocausta; tunc imponent super altare tuum vitulos.", "kjv": "Then shalt thou be pleased with the sacrifices of righteousness, with burnt offering and whole burnt offering: then shall they offer bullocks upon thine altar.", "esv": "then you will delight in right sacrifices, in burnt offerings and whole burnt offerings; then bulls will be offered on your altar.", "rsv": "then thou wilt delight in right sacrifices, in burnt offerings and whole burnt offerings; then bulls will be offered on thy altar." }
    ]
  },
  {
    "psalm": 91,
    "title": "Psalm 91",
    "superscript": "He Who Dwells in the Shadow of the Almighty",
    "verses": [
      { "verse": 1, "hebrew": "יֹשֵׁב בְּסֵתֶר עֶלְיוֹן בְּצֵל שַׁדַּי יִתְלוֹנָן׃", "latin": "Qui habitat in adjutorio Altissimi, in protectione Dei caeli commorabitur.", "kjv": "He that dwelleth in the secret place of the most High shall abide under the shadow of the Almighty.", "esv": "He who dwells in the shelter of the Most High will abide in the shadow of the Almighty.", "rsv": "He who dwells in the shelter of the Most High, who abides in the shadow of the Almighty," },
      { "verse": 2, "hebrew": "אֹמַר לַיהוָה מַחְסִי וּמְצוּדָתִי אֱלֹהַי אֶבְטַח בּוֹ׃", "latin": "Dicet Domino: Susceptor meus es tu et refugium meum; Deus meus, sperabo in eum.", "kjv": "I will say of the LORD, He is my refuge and my fortress: my God; in him will I trust.", "esv": "I will say to the LORD, \"My refuge and my fortress, my God, in whom I trust.\"", "rsv": "will say to the LORD, \"My refuge and my fortress; my God, in whom I trust.\"" },
      { "verse": 3, "hebrew": "כִּי הוּא יַצִּילְךָ מִפַּח יָקוּשׁ מִדֶּבֶר הַוּוֹת׃", "latin": "Quoniam ipse liberavit me de laqueo venantium, et a verbo aspero.", "kjv": "Surely he shall deliver thee from the snare of the fowler, and from the noisome pestilence.", "esv": "For he will deliver you from the snare of the fowler and from the deadly pestilence.", "rsv": "For he will deliver you from the snare of the fowler and from the deadly pestilence;" },
      { "verse": 4, "hebrew": "בְּאֶבְרָתוֹ יָסֶךְ לָךְ וְתַחַת כְּנָפָיו תֶּחְסֶה צִנָּה וְסֹחֵרָה אֲמִתּוֹ׃", "latin": "Scapulis suis obumbrabit tibi, et sub pennis ejus sperabis.", "kjv": "He shall cover thee with his feathers, and under his wings shalt thou trust: his truth shall be thy shield and buckler.", "esv": "He will cover you with his pinions, and under his wings you will find refuge; his faithfulness is a shield and buckler.", "rsv": "he will cover you with his pinions, and under his wings you will find refuge; his faithfulness is a shield and buckler." },
      { "verse": 5, "hebrew": "לֹא תִירָא מִפַּחַד לָיְלָה מֵחֵץ יָעוּף יוֹמָם׃", "latin": "A timore nocturno non timebis; a sagitta volante in die,", "kjv": "Thou shalt not be afraid for the terror by night; nor for the arrow that flieth by day;", "esv": "You will not fear the terror of the night, nor the arrow that flies by day,", "rsv": "You will not fear the terror of the night, nor the arrow that flies by day," },
      { "verse": 6, "hebrew": "מִדֶּבֶר בָּאֹפֶל יַהֲלֹךְ מִקֶּטֶב יָשׁוּד צָהֳרָיִם׃", "latin": "a negotio perambulante in tenebris, ab incursu et daemonio meridiano.", "kjv": "Nor for the pestilence that walketh in darkness; nor for the destruction that wasteth at noonday.", "esv": "nor the pestilence that stalks in darkness, nor the destruction that wastes at noonday.", "rsv": "nor the pestilence that stalks in darkness, nor the destruction that wastes at noonday." },
      { "verse": 7, "hebrew": "יִפֹּל מִצִּדְּךָ אֶלֶף וּרְבָבָה מִימִינֶךָ אֵלֶיךָ לֹא יִגָּשׁ׃", "latin": "Cadent a latere tuo mille, et decem millia a dextris tuis; ad te autem non appropinquabit.", "kjv": "A thousand shall fall at thy side, and ten thousand at thy right hand; but it shall not come nigh thee.", "esv": "A thousand may fall at your side, ten thousand at your right hand, but it will not come near you.", "rsv": "A thousand may fall at your side, ten thousand at your right hand; but it will not come near you." },
      { "verse": 8, "hebrew": "רַק בְּעֵינֶיךָ תַבִּיט וְשִׁלֻּמַת רְשָׁעִים תִּרְאֶה׃", "latin": "Verumtamen oculis tuis considerabis, et retributionem peccatorum videbis.", "kjv": "Only with thine eyes shalt thou behold and see the reward of the wicked.", "esv": "You will only look with your eyes and see the recompense of the wicked.", "rsv": "You will only look with your eyes and see the recompense of the wicked." },
      { "verse": 9, "hebrew": "כִּי אַתָּה יְהוָה מַחְסִי עֶלְיוֹן שַׂמְתָּ מְעוֹנֶךָ׃", "latin": "Quoniam tu es, Domine, spes mea; Altissimum posuisti refugium tuum.", "kjv": "Because thou hast made the LORD, which is my refuge, even the most High, thy habitation;", "esv": "Because you have made the LORD your dwelling place— the Most High, who is my refuge—", "rsv": "Because you have made the LORD your refuge, the Most High your habitation," },
      { "verse": 10, "hebrew": "לֹא תְאֻנֶּה אֵלֶיךָ רָעָה וְנֶגַע לֹא יִקְרַב בְּאָהֳלֶךָ׃", "latin": "Non accedet ad te malum; et flagellum non appropinquabit tabernaculo tuo.", "kjv": "There shall no evil befall thee, neither shall any plague come nigh thy dwelling.", "esv": "no evil shall be allowed to befall you, no plague come near your tent.", "rsv": "no evil shall befall you, no scourge come near your tent." },
      { "verse": 11, "hebrew": "כִּי מַלְאָכָיו יְצַוֶּה לָּךְ לִשְׁמָרְךָ בְּכָל דְּרָכֶיךָ׃", "latin": "Quoniam angelis suis mandavit de te, ut custodiant te in omnibus viis tuis.", "kjv": "For he shall give his angels charge over thee, to keep thee in all thy ways.", "esv": "For he will command his angels concerning you to guard you in all your ways.", "rsv": "For he will give his angels charge of you to guard you in all your ways." },
      { "verse": 12, "hebrew": "עַל כַּפַּיִם יִשָּׂאוּנְךָ פֶּן תִּגֹּף בָּאֶבֶן רַגְלֶךָ׃", "latin": "In manibus portabunt te, ne forte offendas ad lapidem pedem tuum.", "kjv": "They shall bear thee up in their hands, lest thou dash thy foot against a stone.", "esv": "On their hands they will bear you up, lest you strike your foot against a stone.", "rsv": "On their hands they will bear you up, lest you dash your foot against a stone." },
      { "verse": 13, "hebrew": "עַל שַׁחַל וָפֶתֶן תִּדְרֹךְ תִּרְמֹס כְּפִיר וְתַנִּין׃", "latin": "Super aspidem et basiliscum ambulabis, et conculcabis leonem et draconem.", "kjv": "Thou shalt tread upon the lion and adder: the young lion and the dragon shalt thou trample under feet.", "esv": "You will tread on the lion and the adder; the young lion and the serpent you will trample underfoot.", "rsv": "You will tread on the lion and the adder, the young lion and the serpent you will trample under foot." },
      { "verse": 14, "hebrew": "כִּי בִי חָשַׁק וַאֲפַלְּטֵהוּ אֲשַׂגְּבֵהוּ כִּי יָדַע שְׁמִי׃", "latin": "Quoniam in me speravit, liberabo eum; protegam eum, quoniam cognovit nomen meum.", "kjv": "Because he hath set his love upon me, therefore will I deliver him: I will set him on high, because he hath known my name.", "esv": "\"Because he holds fast to me in love, I will deliver him; I will protect him, because he knows my name.", "rsv": "\"Because he cleaves to me in love, I will deliver him; I will protect him, because he knows my name." },
      { "verse": 15, "hebrew": "יִקְרָאֵנִי וְאֶעֱנֵהוּ עִמּוֹ אָנֹכִי בְצָרָה אֲחַלְּצֵהוּ וַאֲכַבְּדֵהוּ׃", "latin": "Clamabit ad me, et ego exaudiam eum; cum ipso sum in tribulatione; eripiam eum et glorificabo eum.", "kjv": "He shall call upon me, and I will answer him: I will be with him in trouble; I will deliver him, and honour him.", "esv": "When he calls to me, I will answer him; I will be with him in trouble; I will rescue him and honor him.", "rsv": "When he calls to me, I will answer him; I will be with him in trouble, I will rescue him and honor him." },
      { "verse": 16, "hebrew": "אֹרֶךְ יָמִים אַשְׂבִּיעֵהוּ וְאַרְאֵהוּ בִּישׁוּעָתִי׃", "latin": "Longitudine dierum replebo eum; et ostendam illi salutare meum.", "kjv": "With long life will I satisfy him, and shew him my salvation.", "esv": "With long life I will satisfy him and show him my salvation.\"", "rsv": "With long life I will satisfy him, and show him my salvation.\"" }
    ]
  },
  {
    "psalm": 150,
    "title": "Psalm 150",
    "superscript": "Laudate Dominum — The Great Doxology",
    "verses": [
      { "verse": 1, "hebrew": "הַלְלוּיָהּ הַלְלוּ אֵל בְּקָדְשׁוֹ הַלְלוּהוּ בִּרְקִיעַ עֻזּוֹ׃", "latin": "Alleluia. Laudate Dominum in sanctis ejus; laudate eum in firmamento virtutis ejus.", "kjv": "Praise ye the LORD. Praise God in his sanctuary: praise him in the firmament of his power.", "esv": "Praise the LORD! Praise God in his sanctuary; praise him in his mighty heavens!", "rsv": "Praise the LORD! Praise God in his sanctuary; praise him in his mighty firmament!" },
      { "verse": 2, "hebrew": "הַלְלוּהוּ בִגְבוּרֹתָיו הַלְלוּהוּ כְּרֹב גֻּדְלוֹ׃", "latin": "Laudate eum in virtutibus ejus; laudate eum secundum multitudinem magnitudinis ejus.", "kjv": "Praise him for his mighty acts: praise him according to his excellent greatness.", "esv": "Praise him for his mighty deeds; praise him according to his excellent greatness!", "rsv": "Praise him for his mighty deeds; praise him according to his exceeding greatness!" },
      { "verse": 3, "hebrew": "הַלְלוּהוּ בְּתֵקַע שׁוֹפָר הַלְלוּהוּ בְּנֵבֶל וְכִנּוֹר׃", "latin": "Laudate eum in sono tubae; laudate eum in psalterio et cithara.", "kjv": "Praise him with the sound of the trumpet: praise him with the psaltery and harp.", "esv": "Praise him with trumpet sound; praise him with lute and harp!", "rsv": "Praise him with trumpet sound; praise him with lute and harp!" },
      { "verse": 4, "hebrew": "הַלְלוּהוּ בְתֹף וּמָחוֹל הַלְלוּהוּ בְּמִנִּים וְעֻגָב׃", "latin": "Laudate eum in tympano et choro; laudate eum in chordis et organo.", "kjv": "Praise him with the timbrel and dancing: praise him with stringed instruments and organs.", "esv": "Praise him with tambourine and dance; praise him with strings and pipe!", "rsv": "Praise him with timbrel and dance; praise him with strings and pipe!" },
      { "verse": 5, "hebrew": "הַלְלוּהוּ בְצִלְצְלֵי שָׁמַע הַלְלוּהוּ בְּצִלְצְלֵי תְרוּעָה׃", "latin": "Laudate eum in cymbalis benesonantibus; laudate eum in cymbalis jubilationis:", "kjv": "Praise him upon the loud cymbals: praise him upon the high sounding cymbals.", "esv": "Praise him with sounding cymbals; praise him with loud clashing cymbals!", "rsv": "Praise him with sounding cymbals; praise him with loud clashing cymbals!" },
      { "verse": 6, "hebrew": "כֹּל הַנְּשָׁמָה תְּהַלֵּל יָהּ הַלְלוּיָהּ׃", "latin": "omnis spiritus laudet Dominum. Alleluia.", "kjv": "Let every thing that hath breath praise the LORD. Praise ye the LORD.", "esv": "Let everything that has breath praise the LORD! Praise the LORD!", "rsv": "Let everything that breathes praise the LORD! Praise the LORD!" }
    ]
  }
]

def main():
    OUT.write_text(
        json.dumps(PSALMS, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    total_verses = sum(len(p["verses"]) for p in PSALMS)
    print(f"✓ Wrote {len(PSALMS)} psalms ({total_verses} verses) → {OUT}")
    print()
    print("NOTE: This starter file contains 5 psalms (1, 22, 23, 51, 91, 150).")
    print("To download all 150 psalms, run:  python generate_data.py")

if __name__ == "__main__":
    main()
