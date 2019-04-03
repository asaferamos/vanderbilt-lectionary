#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, csv

if len(sys.argv) < 3:
    sys.exit('Missing arguments')

def translate():
    toArgument = sys.argv[2].split("to=")
    with open(sys.argv[1], 'r') as fileReader:
        reader = csv.reader(
                    fileReader, delimiter=';',
                    quotechar='"',
                    quoting=csv.QUOTE_MINIMAL
        )
        for line in reader:
            newline = []
            for col in line:
                newline.append(translateText(col,toArgument[1]))

def translateText(text,to):
    texts = {
        'Proper' 							: 'Próprio',
		'All Saints Day' 					: 'Dia de todos os Santos',
		'Annunciation of the Lord'			: 'Anunciação de Cristo',
		'Ascension of the Lord' 			: 'Ascensão do Senhor',
		'Ash Wednesday' 					: 'Quarta-feira de Cinzas',
		'Baptism of the Lord' 				: 'Batismo do Senhor',
		'Day of Pentecost' 					: 'Dia de Pentecostes',
		'Easter Evening' 					: 'Noite de páscoa',
		'Easter Vigil' 						: 'Vigília de Páscoa',
		'Epiphany of the Lord'				: 'Epifania',
		'Fifth Sunday after the Epiphany'	: 'Quinto domingo após a Epifania',
		'Fifth Sunday in Lent' 				: 'Quinto domingo na Quaresma',
		'Fifth Sunday of Easter'			: 'Quinto domingo de Páscoa',
		'First Sunday after Christmas Day'	: 'Primeiro domingo após o Natal',
		'First Sunday in Lent'				: 'Primeiro domingo na Quaresma',
		'First Sunday of Advent'			: 'Primeiro domingo de Advento',
		'Fourth Sunday after the Epiphany'	: 'Quarto domingo após a Epifania',
		'Fourth Sunday in Lent'				: 'Quarto domingo na Quaresma',
		'Fourth Sunday of Advent'			: 'Quarto domingo de Advento',
		'Fourth Sunday of Easter'			: 'Quarto domingo de Páscoa',
		'Good Friday'						: 'Sexta-Feira Santa',
		'Holy Saturday' 					: 'Sábado Santo',
		'Liturgy of the Palms' 				: 'Liturgy of the Palms',
		'Liturgy of the Passion' 			: 'Liturgy of the Passion',
		'Maundy Thursday' 					: 'Quinta-Feira Santa',
		'Monday of Holy Week' 				: 'Segunda-Feira da Semana Santa',
		'Nativity of the Lord' 				: 'Nativity of the Lord',
		'New Year\'s Day' 					: 'Dia de Ano Novo',
		'Reign of Christ' 					: 'Reino de Cristo',
		'Resurrection of the Lord'			: 'Ressurreição de Cristo',
		'Second Sunday after the Epiphany'	: 'Segundo domingo após a Epifania',
		'Second Sunday in Lent' 			: 'Segundo domingo na Quaresma',
		'Second Sunday of Advent' 			: 'Segundo domingo do Advento',
		'Second Sunday of Easter' 			: 'Segundo domingo de Páscoa',
		'Seventh Sunday of Easter'			: 'Sétimo domingo de Páscoa',
		'Sixth Sunday of Easter' 			: 'Sexto domingo de Páscoa',
		'Third Sunday after the Epiphany'	: 'Terceiro domingo após a Epifania',
		'Third Sunday in Lent' 				: 'Terceiro domingo em Quaresma',
		'Third Sunday of Advent' 			: 'Terceiro domingo de Advento',
		'Third Sunday of Easter' 			: 'Terceiro domingo de Páscoa',
		'Transfiguration Sunday' 			: 'Domingo da Transfiguração',
		'Trinity Sunday'		 			: 'Domingo da Trindade',
		'Tuesday of Holy Week'	 			: 'Terça-feira da Semana Santa',
		'Visitation of Mary to Elizabeth '	: 'Visita de Maria a Elizabeth',
		'Wednesday of Holy Week' 			: 'Quarta-feira da Semana Santa',

        'Sunday'      : 'Domingo',
		'Monday'      : 'Segunda',
		'Tuesday'     : 'Terça',
		'Wednesday'   : 'Quarta',
		'Thursday'    : 'Quinta',
		'Friday'      : 'Sexta',
		'Saturday'    : 'Sábado',
		'January'     : 'Janeiro',
		'February'    : 'Fevereiro',
		'March'       : 'Março',
		'April'       : 'Abril',
		'May'         : 'Maio',
		'June'        : 'Junho',
		'July'        : 'Julho',
		'August'      : 'Agosto',
		'September'   : 'Setembro',
		'October'     : 'Outubro',
		'November'    : 'Novembro',
		'December'    : 'Dezembro',

        'Genesis' 			: 'Gênesis',
		'Exodus' 			: 'Êxodo',
		'Leviticus' 		: 'Levítico',
		'Numbers' 			: 'Números',
		'Deuteronomy' 		: 'Deuteronômio',
		'Joshua' 			: 'Josué',
		'Judges' 			: 'Juízes',
		'Ruth' 				: 'Rute',
		'1 Samuel' 			: '1 Samuel',
		'2 Samuel' 			: '2 Samuel',
		'1 Kings' 			: '1 Reis',
		'2 Kings' 			: '2 Reis',
		'1 Chronicles' 		: '1 Crônicas',
		'2 Chronicles' 		: '2 Crônicas',
		'Ezra' 				: 'Esdras',
		'Nehemiah' 			: 'Neemias',
		'Esther' 			: 'Ester',
		'Job' 				: 'Jó',
		'Psalm' 			: 'Salmos',
		'Proverbs' 			: 'Provérbios',
		'Ecclesiastes'  	: 'Eclesiastes',
		'Song of Solomon' 	: 'Cantares de Salomão',
		'Isaiah' 			: 'Isaías',
		'Jeremiah' 			: 'Jeremias',
		'Lamentations' 		: 'Lamentações',
		'Ezekiel' 			: 'Ezequiel',
		'Daniel' 			: 'Daniel',
		'Hosea' 			: 'Oseias',
		'Joel' 				: 'Joel',
		'Amos' 				: 'Amós',
		'Obadiah' 			: 'Obadias',
		'Jonah' 			: 'Jonas',
		'Micah' 			: 'Miqueias',
		'Nahum' 			: 'Naum',
		'Habakkuk' 			: 'Habacuque',
		'Zephaniah' 		: 'Sofonias',
		'Haggai' 			: 'Ageu',
		'Zechariah' 		: 'Zacarias',
		'Malachi' 			: 'Malaquias',
		'Matthew' 			: 'Mateus',
		'Mark' 				: 'Marcos',
		'Luke' 				: 'Lucas',
		'John' 				: 'João',
		'Acts' 				: 'Atos',
		'Romans' 			: 'Romanos',
		'2 Corinthians' 	: '2 Coríntios',
		'1 Corinthians' 	: '1 Coríntios',
		'Galatians' 		: 'Gálatas',
		'Ephesians' 		: 'Efésios',
		'Philippians' 		: 'Filipenses',
		'Colossians' 		: 'Colossenses',
		'1 Thessalonians'	: '1 Tessalonicenses',
		'2 Thessalonians' 	: '2 Tessalonicenses',
		'1 Timothy' 		: '1 Timóteo',
		'2 Timothy' 		: '2 Timóteo',
		'Titus' 			: 'Tito',
		'Philemon' 			: 'Filêmon',
		'Hebrews' 			: 'Hebreus',
		'James' 			: 'Tiago',
		'1 Peter' 			: '1 Pedro',
		'2 Peter' 			: '2 Pedro',
		'1 John' 			: '1 João',
		'2 John' 			: '2 João',
		'3 John' 			: '3 João',
		'Jude' 				: 'Judas',
		'Revelation' 		: 'Apocalipse',
		' or ' 				: ' ou ',
		' and '				: ' e '
    }

    newText = ""
    for key,val in texts.items():
        newText = text.replace(key,val)
        if newText != text:
            return newText

    return text

translate()