;--------------------------------------------------------
; File Created by SDCC : free open source ANSI-C Compiler
; Version 3.5.0 #9253 (Nov 15 2015) (Linux)
; This file was generated Mon Mar  7 22:49:32 2016
;--------------------------------------------------------
; PIC16 port for the Microchip 16-bit core micros
;--------------------------------------------------------
	list	p=18f4550
	radix	dec
	CONFIG	FOSC=HSPLL_HS
	CONFIG	WDT=OFF
	CONFIG	LVP=OFF
	CONFIG	PBADEN=OFF
	CONFIG	PLLDIV=5
	CONFIG	USBDIV=1
	CONFIG	CPUDIV=OSC1_PLL2
	CONFIG	FCMEN=OFF
	CONFIG	PWRT=ON
	CONFIG	BOR=ON
	CONFIG	VREGEN=ON
	CONFIG	MCLRE=OFF
	CONFIG	CCP2MX=ON
	CONFIG	STVREN=ON
	CONFIG	XINST=OFF


;--------------------------------------------------------
; public variables in this module
;--------------------------------------------------------
	global	_TMR0_ini
	global	_servo_active
	global	_TMR0_isr
	global	_RX_isr
	global	_TX_isr
	global	__putc
	global	_puts
	global	_getch
	global	_setup_UART
	global	_Mover
	global	_pulse
	global	_milisec
	global	_tx_buf
	global	_tx_next
	global	_tx_send
	global	_rx_buf
	global	_rx_next
	global	_rx_read
	global	_high_ISR
	global	_main

;--------------------------------------------------------
; extern variables in this module
;--------------------------------------------------------
	extern	__gptrget1
	extern	_SPPCFGbits
	extern	_SPPEPSbits
	extern	_SPPCONbits
	extern	_UFRMLbits
	extern	_UFRMHbits
	extern	_UIRbits
	extern	_UIEbits
	extern	_UEIRbits
	extern	_UEIEbits
	extern	_USTATbits
	extern	_UCONbits
	extern	_UADDRbits
	extern	_UCFGbits
	extern	_UEP0bits
	extern	_UEP1bits
	extern	_UEP2bits
	extern	_UEP3bits
	extern	_UEP4bits
	extern	_UEP5bits
	extern	_UEP6bits
	extern	_UEP7bits
	extern	_UEP8bits
	extern	_UEP9bits
	extern	_UEP10bits
	extern	_UEP11bits
	extern	_UEP12bits
	extern	_UEP13bits
	extern	_UEP14bits
	extern	_UEP15bits
	extern	_PORTAbits
	extern	_PORTBbits
	extern	_PORTCbits
	extern	_PORTDbits
	extern	_PORTEbits
	extern	_LATAbits
	extern	_LATBbits
	extern	_LATCbits
	extern	_LATDbits
	extern	_LATEbits
	extern	_DDRAbits
	extern	_TRISAbits
	extern	_DDRBbits
	extern	_TRISBbits
	extern	_DDRCbits
	extern	_TRISCbits
	extern	_DDRDbits
	extern	_TRISDbits
	extern	_DDREbits
	extern	_TRISEbits
	extern	_OSCTUNEbits
	extern	_PIE1bits
	extern	_PIR1bits
	extern	_IPR1bits
	extern	_PIE2bits
	extern	_PIR2bits
	extern	_IPR2bits
	extern	_EECON1bits
	extern	_RCSTAbits
	extern	_TXSTAbits
	extern	_T3CONbits
	extern	_CMCONbits
	extern	_CVRCONbits
	extern	_CCP1ASbits
	extern	_ECCP1ASbits
	extern	_CCP1DELbits
	extern	_ECCP1DELbits
	extern	_BAUDCONbits
	extern	_BAUDCTLbits
	extern	_CCP2CONbits
	extern	_CCP1CONbits
	extern	_ECCP1CONbits
	extern	_ADCON2bits
	extern	_ADCON1bits
	extern	_ADCON0bits
	extern	_SSPCON2bits
	extern	_SSPCON1bits
	extern	_SSPSTATbits
	extern	_T2CONbits
	extern	_T1CONbits
	extern	_RCONbits
	extern	_WDTCONbits
	extern	_HLVDCONbits
	extern	_LVDCONbits
	extern	_OSCCONbits
	extern	_T0CONbits
	extern	_STATUSbits
	extern	_INTCON3bits
	extern	_INTCON2bits
	extern	_INTCONbits
	extern	_STKPTRbits
	extern	_SPPDATA
	extern	_SPPCFG
	extern	_SPPEPS
	extern	_SPPCON
	extern	_UFRM
	extern	_UFRML
	extern	_UFRMH
	extern	_UIR
	extern	_UIE
	extern	_UEIR
	extern	_UEIE
	extern	_USTAT
	extern	_UCON
	extern	_UADDR
	extern	_UCFG
	extern	_UEP0
	extern	_UEP1
	extern	_UEP2
	extern	_UEP3
	extern	_UEP4
	extern	_UEP5
	extern	_UEP6
	extern	_UEP7
	extern	_UEP8
	extern	_UEP9
	extern	_UEP10
	extern	_UEP11
	extern	_UEP12
	extern	_UEP13
	extern	_UEP14
	extern	_UEP15
	extern	_PORTA
	extern	_PORTB
	extern	_PORTC
	extern	_PORTD
	extern	_PORTE
	extern	_LATA
	extern	_LATB
	extern	_LATC
	extern	_LATD
	extern	_LATE
	extern	_DDRA
	extern	_TRISA
	extern	_DDRB
	extern	_TRISB
	extern	_DDRC
	extern	_TRISC
	extern	_DDRD
	extern	_TRISD
	extern	_DDRE
	extern	_TRISE
	extern	_OSCTUNE
	extern	_PIE1
	extern	_PIR1
	extern	_IPR1
	extern	_PIE2
	extern	_PIR2
	extern	_IPR2
	extern	_EECON1
	extern	_EECON2
	extern	_EEDATA
	extern	_EEADR
	extern	_RCSTA
	extern	_TXSTA
	extern	_TXREG
	extern	_RCREG
	extern	_SPBRG
	extern	_SPBRGH
	extern	_T3CON
	extern	_TMR3
	extern	_TMR3L
	extern	_TMR3H
	extern	_CMCON
	extern	_CVRCON
	extern	_CCP1AS
	extern	_ECCP1AS
	extern	_CCP1DEL
	extern	_ECCP1DEL
	extern	_BAUDCON
	extern	_BAUDCTL
	extern	_CCP2CON
	extern	_CCPR2
	extern	_CCPR2L
	extern	_CCPR2H
	extern	_CCP1CON
	extern	_ECCP1CON
	extern	_CCPR1
	extern	_CCPR1L
	extern	_CCPR1H
	extern	_ADCON2
	extern	_ADCON1
	extern	_ADCON0
	extern	_ADRES
	extern	_ADRESL
	extern	_ADRESH
	extern	_SSPCON2
	extern	_SSPCON1
	extern	_SSPSTAT
	extern	_SSPADD
	extern	_SSPBUF
	extern	_T2CON
	extern	_PR2
	extern	_TMR2
	extern	_T1CON
	extern	_TMR1
	extern	_TMR1L
	extern	_TMR1H
	extern	_RCON
	extern	_WDTCON
	extern	_HLVDCON
	extern	_LVDCON
	extern	_OSCCON
	extern	_T0CON
	extern	_TMR0
	extern	_TMR0L
	extern	_TMR0H
	extern	_STATUS
	extern	_FSR2L
	extern	_FSR2H
	extern	_PLUSW2
	extern	_PREINC2
	extern	_POSTDEC2
	extern	_POSTINC2
	extern	_INDF2
	extern	_BSR
	extern	_FSR1L
	extern	_FSR1H
	extern	_PLUSW1
	extern	_PREINC1
	extern	_POSTDEC1
	extern	_POSTINC1
	extern	_INDF1
	extern	_WREG
	extern	_FSR0L
	extern	_FSR0H
	extern	_PLUSW0
	extern	_PREINC0
	extern	_POSTDEC0
	extern	_POSTINC0
	extern	_INDF0
	extern	_INTCON3
	extern	_INTCON2
	extern	_INTCON
	extern	_PROD
	extern	_PRODL
	extern	_PRODH
	extern	_TABLAT
	extern	_TBLPTR
	extern	_TBLPTRL
	extern	_TBLPTRH
	extern	_TBLPTRU
	extern	_PC
	extern	_PCL
	extern	_PCLATH
	extern	_PCLATU
	extern	_STKPTR
	extern	_TOS
	extern	_TOSL
	extern	_TOSH
	extern	_TOSU
	extern	__mulint

;--------------------------------------------------------
;	Equates to used internal registers
;--------------------------------------------------------
STATUS	equ	0xfd8
PCLATH	equ	0xffa
PCLATU	equ	0xffb
WREG	equ	0xfe8
BSR	equ	0xfe0
FSR0L	equ	0xfe9
FSR0H	equ	0xfea
FSR1L	equ	0xfe1
FSR2L	equ	0xfd9
INDF0	equ	0xfef
POSTINC0	equ	0xfee
POSTINC1	equ	0xfe6
POSTDEC1	equ	0xfe5
PREINC1	equ	0xfe4
PLUSW2	equ	0xfdb
PRODL	equ	0xff3
PRODH	equ	0xff4


	idata
_servo_active	db	0x00, 0x00
_pulse	db	0xe8, 0x03, 0xe2, 0x04, 0xdc, 0x05, 0xd6, 0x06, 0xd0, 0x07
_milisec	db	0x00, 0x00
_tx_next	db	0x00, 0x00
_tx_send	db	0x00, 0x00
_rx_next	db	0x00, 0x00
_rx_read	db	0x00, 0x00


; Internal registers
.registers	udata_ovr	0x0000
r0x00	res	1
r0x01	res	1
r0x02	res	1
r0x03	res	1
r0x04	res	1
r0x05	res	1
r0x06	res	1
r0x07	res	1

udata_main_0	udata
_TMR0_ini	res	2

udata_main_1	udata
_rx_buf	res	256

udata_main_2	udata
_tx_buf	res	256

;--------------------------------------------------------
; interrupt vector
;--------------------------------------------------------

;--------------------------------------------------------
; global & static initialisations
;--------------------------------------------------------
; ; Starting pCode block for absolute section
; ;-----------------------------------------
S_main_ivec_0x1_high_ISR	code	0X000008
ivec_0x1_high_ISR:
	GOTO	_high_ISR

; I code from now on!
; ; Starting pCode block
S_main__main	code
_main:
;	.line	334; main.c	T0CON = 0b00001000;
	MOVLW	0x08
	MOVWF	_T0CON
;	.line	335; main.c	enable_global_ints;
	BSF	_INTCONbits, 7
;	.line	337; main.c	enable_TMR0_int;
	BSF	_INTCONbits, 5
;	.line	338; main.c	start_TMR0;
	BSF	_T0CONbits, 7
;	.line	342; main.c	TRISA = 0;
	CLRF	_TRISA
;	.line	343; main.c	PORTA = 0;	
	CLRF	_PORTA
;	.line	344; main.c	TRISB = 0;
	CLRF	_TRISB
;	.line	345; main.c	PORTB = 0;
	CLRF	_PORTB
;	.line	346; main.c	TRISC = 0;
	CLRF	_TRISC
;	.line	347; main.c	PORTC = 0;
	CLRF	_PORTC
;	.line	348; main.c	TRISD = 0;
	CLRF	_TRISD
;	.line	349; main.c	PORTD = 0;
	CLRF	_PORTD
_00296_DS_:
;	.line	363; main.c	while (1)
	BRA	_00296_DS_
	RETURN	

; ; Starting pCode block
S_main__Mover	code
_Mover:
;	.line	239; main.c	void Mover (void)
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	MOVFF	r0x02, POSTDEC1
;	.line	241; main.c	char ch = getch ();
	CALL	_getch
	MOVWF	r0x00
;	.line	242; main.c	if (ch == 'a' || ch == 'c' || ch == 'e' || ch == 'g' || ch == 'i')
	CLRF	r0x01
	MOVF	r0x00, W
	XORLW	0x61
	BNZ	_00256_DS_
	INCF	r0x01, F
_00256_DS_:
	MOVF	r0x01, W
	BNZ	_00177_DS_
	MOVF	r0x00, W
	XORLW	0x63
	BZ	_00177_DS_
	MOVF	r0x00, W
	XORLW	0x65
	BZ	_00177_DS_
	MOVF	r0x00, W
	XORLW	0x67
	BZ	_00177_DS_
	MOVF	r0x00, W
	XORLW	0x69
	BZ	_00177_DS_
	BRA	_00178_DS_
_00177_DS_:
;	.line	245; main.c	if (ch == 'a')
	MOVF	r0x01, W
	BZ	_00168_DS_
	BANKSEL	_pulse
;	.line	249; main.c	pulse[0]-=20;
	MOVF	_pulse, W, B
	ADDLW	0xec
	MOVWF	r0x01
	MOVLW	0xff
	BANKSEL	(_pulse + 1)
	ADDWFC	(_pulse + 1), W, B
	MOVWF	r0x02
	MOVF	r0x01, W
	BANKSEL	_pulse
	MOVWF	_pulse, B
	MOVF	r0x02, W
	BANKSEL	(_pulse + 1)
	MOVWF	(_pulse + 1), B
_00168_DS_:
;	.line	253; main.c	if (ch == 'c')
	MOVF	r0x00, W
	XORLW	0x63
	BNZ	_00170_DS_
_00266_DS_:
	BANKSEL	(_pulse + 2)
;	.line	257; main.c	pulse[1]-=20;
	MOVF	(_pulse + 2), W, B
	ADDLW	0xec
	MOVWF	r0x01
	MOVLW	0xff
	BANKSEL	(_pulse + 3)
	ADDWFC	(_pulse + 3), W, B
	MOVWF	r0x02
	MOVF	r0x01, W
	BANKSEL	(_pulse + 2)
	MOVWF	(_pulse + 2), B
	MOVF	r0x02, W
	BANKSEL	(_pulse + 3)
	MOVWF	(_pulse + 3), B
_00170_DS_:
;	.line	261; main.c	if (ch == 'e')
	MOVF	r0x00, W
	XORLW	0x65
	BNZ	_00172_DS_
_00268_DS_:
	BANKSEL	(_pulse + 4)
;	.line	265; main.c	pulse[2]-=20;
	MOVF	(_pulse + 4), W, B
	ADDLW	0xec
	MOVWF	r0x01
	MOVLW	0xff
	BANKSEL	(_pulse + 5)
	ADDWFC	(_pulse + 5), W, B
	MOVWF	r0x02
	MOVF	r0x01, W
	BANKSEL	(_pulse + 4)
	MOVWF	(_pulse + 4), B
	MOVF	r0x02, W
	BANKSEL	(_pulse + 5)
	MOVWF	(_pulse + 5), B
_00172_DS_:
;	.line	269; main.c	if (ch == 'g')
	MOVF	r0x00, W
	XORLW	0x67
	BNZ	_00174_DS_
_00270_DS_:
	BANKSEL	(_pulse + 6)
;	.line	273; main.c	pulse[3]-=20;
	MOVF	(_pulse + 6), W, B
	ADDLW	0xec
	MOVWF	r0x01
	MOVLW	0xff
	BANKSEL	(_pulse + 7)
	ADDWFC	(_pulse + 7), W, B
	MOVWF	r0x02
	MOVF	r0x01, W
	BANKSEL	(_pulse + 6)
	MOVWF	(_pulse + 6), B
	MOVF	r0x02, W
	BANKSEL	(_pulse + 7)
	MOVWF	(_pulse + 7), B
_00174_DS_:
;	.line	277; main.c	if (ch == 'i')
	MOVF	r0x00, W
	XORLW	0x69
	BNZ	_00178_DS_
_00272_DS_:
	BANKSEL	(_pulse + 8)
;	.line	281; main.c	pulse[4]-=20;
	MOVF	(_pulse + 8), W, B
	ADDLW	0xec
	MOVWF	r0x01
	MOVLW	0xff
	BANKSEL	(_pulse + 9)
	ADDWFC	(_pulse + 9), W, B
	MOVWF	r0x02
	MOVF	r0x01, W
	BANKSEL	(_pulse + 8)
	MOVWF	(_pulse + 8), B
	MOVF	r0x02, W
	BANKSEL	(_pulse + 9)
	MOVWF	(_pulse + 9), B
_00178_DS_:
;	.line	286; main.c	if (ch == 'b' || ch == 'd' || ch == 'f' || ch == 'h' || ch == 'j')
	CLRF	r0x01
	MOVF	r0x00, W
	XORLW	0x62
	BNZ	_00274_DS_
	INCF	r0x01, F
_00274_DS_:
	MOVF	r0x01, W
	BNZ	_00193_DS_
	MOVF	r0x00, W
	XORLW	0x64
	BZ	_00193_DS_
	MOVF	r0x00, W
	XORLW	0x66
	BZ	_00193_DS_
	MOVF	r0x00, W
	XORLW	0x68
	BZ	_00193_DS_
	MOVF	r0x00, W
	XORLW	0x6a
	BZ	_00193_DS_
	BRA	_00199_DS_
_00193_DS_:
;	.line	288; main.c	if (ch == 'b')
	MOVF	r0x01, W
	BZ	_00184_DS_
	BANKSEL	_pulse
;	.line	292; main.c	pulse[0]+=20;
	MOVF	_pulse, W, B
	ADDLW	0x14
	MOVWF	r0x01
	MOVLW	0x00
	BANKSEL	(_pulse + 1)
	ADDWFC	(_pulse + 1), W, B
	MOVWF	r0x02
	MOVF	r0x01, W
	BANKSEL	_pulse
	MOVWF	_pulse, B
	MOVF	r0x02, W
	BANKSEL	(_pulse + 1)
	MOVWF	(_pulse + 1), B
_00184_DS_:
;	.line	296; main.c	if (ch == 'd')
	MOVF	r0x00, W
	XORLW	0x64
	BNZ	_00186_DS_
_00284_DS_:
	BANKSEL	(_pulse + 2)
;	.line	300; main.c	pulse[1]+=20;
	MOVF	(_pulse + 2), W, B
	ADDLW	0x14
	MOVWF	r0x01
	MOVLW	0x00
	BANKSEL	(_pulse + 3)
	ADDWFC	(_pulse + 3), W, B
	MOVWF	r0x02
	MOVF	r0x01, W
	BANKSEL	(_pulse + 2)
	MOVWF	(_pulse + 2), B
	MOVF	r0x02, W
	BANKSEL	(_pulse + 3)
	MOVWF	(_pulse + 3), B
_00186_DS_:
;	.line	304; main.c	if (ch == 'f')
	MOVF	r0x00, W
	XORLW	0x66
	BNZ	_00188_DS_
_00286_DS_:
	BANKSEL	(_pulse + 4)
;	.line	308; main.c	pulse[2]+=20;
	MOVF	(_pulse + 4), W, B
	ADDLW	0x14
	MOVWF	r0x01
	MOVLW	0x00
	BANKSEL	(_pulse + 5)
	ADDWFC	(_pulse + 5), W, B
	MOVWF	r0x02
	MOVF	r0x01, W
	BANKSEL	(_pulse + 4)
	MOVWF	(_pulse + 4), B
	MOVF	r0x02, W
	BANKSEL	(_pulse + 5)
	MOVWF	(_pulse + 5), B
_00188_DS_:
;	.line	312; main.c	if (ch == 'h')
	MOVF	r0x00, W
	XORLW	0x68
	BNZ	_00190_DS_
_00288_DS_:
	BANKSEL	(_pulse + 6)
;	.line	316; main.c	pulse[3]+=20;
	MOVF	(_pulse + 6), W, B
	ADDLW	0x14
	MOVWF	r0x01
	MOVLW	0x00
	BANKSEL	(_pulse + 7)
	ADDWFC	(_pulse + 7), W, B
	MOVWF	r0x02
	MOVF	r0x01, W
	BANKSEL	(_pulse + 6)
	MOVWF	(_pulse + 6), B
	MOVF	r0x02, W
	BANKSEL	(_pulse + 7)
	MOVWF	(_pulse + 7), B
_00190_DS_:
;	.line	320; main.c	if (ch == 'j')
	MOVF	r0x00, W
	XORLW	0x6a
	BNZ	_00199_DS_
_00290_DS_:
	BANKSEL	(_pulse + 8)
;	.line	324; main.c	pulse[4]+=20;
	MOVF	(_pulse + 8), W, B
	ADDLW	0x14
	MOVWF	r0x00
	MOVLW	0x00
	BANKSEL	(_pulse + 9)
	ADDWFC	(_pulse + 9), W, B
	MOVWF	r0x01
	MOVF	r0x00, W
	BANKSEL	(_pulse + 8)
	MOVWF	(_pulse + 8), B
	MOVF	r0x01, W
	BANKSEL	(_pulse + 9)
	MOVWF	(_pulse + 9), B
_00199_DS_:
	MOVFF	PREINC1, r0x02
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_main__setup_UART	code
_setup_UART:
;	.line	214; main.c	void setup_UART (unsigned int brgh, unsigned int spbrg)
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	MOVFF	r0x02, POSTDEC1
	MOVFF	r0x03, POSTDEC1
	MOVLW	0x02
	MOVFF	PLUSW2, r0x00
	MOVLW	0x03
	MOVFF	PLUSW2, r0x01
	MOVLW	0x04
	MOVFF	PLUSW2, r0x02
	MOVLW	0x05
	MOVFF	PLUSW2, r0x03
;	.line	216; main.c	TRISCbits.TRISC6 = 0; 	//TX
	BCF	_TRISCbits, 6
;	.line	217; main.c	TRISCbits.TRISC7 = 1; 	//RX
	BSF	_TRISCbits, 7
;	.line	221; main.c	TXSTA = 0x00;		//reiniciar el estado de TX
	CLRF	_TXSTA
;	.line	222; main.c	TXSTAbits.SYNC = 0; //trabajar asíncronamente
	BCF	_TXSTAbits, 4
;	.line	223; main.c	TXSTAbits.TXEN = 1;	//habilitar TX para enviar
	BSF	_TXSTAbits, 5
;	.line	224; main.c	TXSTAbits.TRMT = 1;	//limpiado del registro de envio
	BSF	_TXSTAbits, 1
;	.line	228; main.c	RCSTA = 0x00;		//reiniciar el estado de RX
	CLRF	_RCSTA
;	.line	229; main.c	RCSTAbits.SPEN = 1;	//habilitar el puerto serial
	BSF	_RCSTAbits, 7
;	.line	230; main.c	RCSTAbits.CREN = 1;	//habilitar RX para recibir
	BSF	_RCSTAbits, 4
;	.line	233; main.c	TXSTAbits.BRGH = brgh;
	MOVF	r0x00, W
	ANDLW	0x01
	RLNCF	WREG, W
	RLNCF	WREG, W
	MOVWF	PRODH
	MOVF	_TXSTAbits, W
	ANDLW	0xfb
	IORWF	PRODH, W
	MOVWF	_TXSTAbits
;	.line	234; main.c	SPBRG = spbrg;
	MOVF	r0x02, W
	MOVWF	_SPBRG
	MOVFF	PREINC1, r0x03
	MOVFF	PREINC1, r0x02
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_main__getch	code
_getch:
;	.line	204; main.c	unsigned char getch (void)
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	BANKSEL	(_rx_read + 1)
;	.line	206; main.c	char ch = rx_buf[rx_read];
	MOVF	(_rx_read + 1), W, B
	MOVWF	POSTDEC1
	BANKSEL	_rx_read
	MOVF	_rx_read, W, B
	MOVWF	POSTDEC1
	MOVLW	0x00
	MOVWF	POSTDEC1
	MOVLW	0x02
	MOVWF	POSTDEC1
	CALL	__mulint
	MOVWF	r0x00
	MOVFF	PRODL, r0x01
	MOVLW	0x04
	ADDWF	FSR1L, F
	MOVLW	LOW(_rx_buf)
	ADDWF	r0x00, F
	MOVLW	HIGH(_rx_buf)
	ADDWFC	r0x01, F
	MOVFF	r0x00, FSR0L
	MOVFF	r0x01, FSR0H
	MOVFF	POSTINC0, r0x00
	MOVFF	INDF0, r0x01
	BANKSEL	_rx_read
;	.line	207; main.c	inc(rx_read);
	INCFSZ	_rx_read, F, B
	BRA	_10295_DS_
	BANKSEL	(_rx_read + 1)
	INCF	(_rx_read + 1), F, B
_10295_DS_:
	BANKSEL	_rx_read
	BCF	_rx_read, 7, B
	BANKSEL	(_rx_read + 1)
	CLRF	(_rx_read + 1), B
;	.line	208; main.c	return ch;
	MOVF	r0x00, W
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_main__puts	code
_puts:
;	.line	191; main.c	void puts (const unsigned char ch[])
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	MOVFF	r0x02, POSTDEC1
	MOVFF	r0x03, POSTDEC1
	MOVFF	r0x04, POSTDEC1
	MOVFF	r0x05, POSTDEC1
	MOVFF	r0x06, POSTDEC1
	MOVFF	r0x07, POSTDEC1
	MOVLW	0x02
	MOVFF	PLUSW2, r0x00
	MOVLW	0x03
	MOVFF	PLUSW2, r0x01
	MOVLW	0x04
	MOVFF	PLUSW2, r0x02
;	.line	194; main.c	do 
	CLRF	r0x03
	CLRF	r0x04
_00149_DS_:
;	.line	196; main.c	_putc (ch[i]);
	MOVF	r0x03, W
	ADDWF	r0x00, W
	MOVWF	r0x05
	MOVF	r0x04, W
	ADDWFC	r0x01, W
	MOVWF	r0x06
	CLRF	WREG
	BTFSC	r0x04, 7
	SETF	WREG
	ADDWFC	r0x02, W
	MOVWF	r0x07
	MOVFF	r0x05, FSR0L
	MOVFF	r0x06, PRODL
	MOVF	r0x07, W
	CALL	__gptrget1
	MOVWF	r0x05
	MOVF	r0x05, W
	MOVWF	POSTDEC1
	CALL	__putc
	MOVF	POSTINC1, F
;	.line	197; main.c	i++;
	INFSNZ	r0x03, F
	INCF	r0x04, F
;	.line	199; main.c	while (ch[i] != '\0');
	MOVF	r0x03, W
	ADDWF	r0x00, W
	MOVWF	r0x05
	MOVF	r0x04, W
	ADDWFC	r0x01, W
	MOVWF	r0x06
	CLRF	WREG
	BTFSC	r0x04, 7
	SETF	WREG
	ADDWFC	r0x02, W
	MOVWF	r0x07
	MOVFF	r0x05, FSR0L
	MOVFF	r0x06, PRODL
	MOVF	r0x07, W
	CALL	__gptrget1
	MOVWF	r0x05
	MOVF	r0x05, W
	BNZ	_00149_DS_
	MOVFF	PREINC1, r0x07
	MOVFF	PREINC1, r0x06
	MOVFF	PREINC1, r0x05
	MOVFF	PREINC1, r0x04
	MOVFF	PREINC1, r0x03
	MOVFF	PREINC1, r0x02
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_main___putc	code
__putc:
;	.line	182; main.c	void _putc (unsigned char ch)
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	MOVFF	r0x02, POSTDEC1
	MOVFF	r0x03, POSTDEC1
	MOVLW	0x02
	MOVFF	PLUSW2, r0x00
	BANKSEL	(_tx_next + 1)
;	.line	184; main.c	tx_buf[tx_next]=ch;
	MOVF	(_tx_next + 1), W, B
	MOVWF	POSTDEC1
	BANKSEL	_tx_next
	MOVF	_tx_next, W, B
	MOVWF	POSTDEC1
	MOVLW	0x00
	MOVWF	POSTDEC1
	MOVLW	0x02
	MOVWF	POSTDEC1
	CALL	__mulint
	MOVWF	r0x01
	MOVFF	PRODL, r0x02
	MOVLW	0x04
	ADDWF	FSR1L, F
	MOVLW	LOW(_tx_buf)
	ADDWF	r0x01, F
	MOVLW	HIGH(_tx_buf)
	ADDWFC	r0x02, F
	CLRF	r0x03
	MOVFF	r0x01, FSR0L
	MOVFF	r0x02, FSR0H
	MOVFF	r0x00, POSTINC0
	MOVFF	r0x03, INDF0
	BANKSEL	_tx_next
;	.line	185; main.c	inc(tx_next);
	INCFSZ	_tx_next, F, B
	BRA	_20296_DS_
	BANKSEL	(_tx_next + 1)
	INCF	(_tx_next + 1), F, B
_20296_DS_:
	BANKSEL	_tx_next
	BCF	_tx_next, 7, B
	BANKSEL	(_tx_next + 1)
	CLRF	(_tx_next + 1), B
;	.line	186; main.c	enable_TX_int;
	BSF	_PIE1bits, 4
	MOVFF	PREINC1, r0x03
	MOVFF	PREINC1, r0x02
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_main__TX_isr	code
_TX_isr:
;	.line	165; main.c	void TX_isr (void)
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	BANKSEL	_tx_send
;	.line	167; main.c	if (tx_send==tx_next)
	MOVF	_tx_send, W, B
	BANKSEL	_tx_next
	XORWF	_tx_next, W, B
	BNZ	_00138_DS_
	BANKSEL	(_tx_send + 1)
	MOVF	(_tx_send + 1), W, B
	BANKSEL	(_tx_next + 1)
	XORWF	(_tx_next + 1), W, B
	BZ	_00139_DS_
_00138_DS_:
	BRA	_00131_DS_
_00139_DS_:
;	.line	169; main.c	disable_TX_int;
	BCF	_PIE1bits, 4
	BRA	_00132_DS_
_00131_DS_:
	BANKSEL	(_tx_send + 1)
;	.line	173; main.c	TXREG = tx_buf[tx_send];
	MOVF	(_tx_send + 1), W, B
	MOVWF	POSTDEC1
	BANKSEL	_tx_send
	MOVF	_tx_send, W, B
	MOVWF	POSTDEC1
	MOVLW	0x00
	MOVWF	POSTDEC1
	MOVLW	0x02
	MOVWF	POSTDEC1
	CALL	__mulint
	MOVWF	r0x00
	MOVFF	PRODL, r0x01
	MOVLW	0x04
	ADDWF	FSR1L, F
	MOVLW	LOW(_tx_buf)
	ADDWF	r0x00, F
	MOVLW	HIGH(_tx_buf)
	ADDWFC	r0x01, F
	MOVFF	r0x00, FSR0L
	MOVFF	r0x01, FSR0H
	MOVFF	POSTINC0, r0x00
	MOVFF	INDF0, r0x01
	MOVF	r0x00, W
	MOVWF	_TXREG
	BANKSEL	_tx_send
;	.line	174; main.c	inc(tx_send);
	INCFSZ	_tx_send, F, B
	BRA	_30297_DS_
	BANKSEL	(_tx_send + 1)
	INCF	(_tx_send + 1), F, B
_30297_DS_:
	BANKSEL	_tx_send
	BCF	_tx_send, 7, B
	BANKSEL	(_tx_send + 1)
	CLRF	(_tx_send + 1), B
_00132_DS_:
;	.line	176; main.c	TX_flag = 0;
	BCF	_PIR1bits, 4
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_main__RX_isr	code
_RX_isr:
;	.line	155; main.c	void RX_isr (void) 
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	MOVFF	r0x02, POSTDEC1
	MOVFF	r0x03, POSTDEC1
	BANKSEL	(_rx_next + 1)
;	.line	157; main.c	rx_buf[rx_next] = RCREG;
	MOVF	(_rx_next + 1), W, B
	MOVWF	POSTDEC1
	BANKSEL	_rx_next
	MOVF	_rx_next, W, B
	MOVWF	POSTDEC1
	MOVLW	0x00
	MOVWF	POSTDEC1
	MOVLW	0x02
	MOVWF	POSTDEC1
	CALL	__mulint
	MOVWF	r0x00
	MOVFF	PRODL, r0x01
	MOVLW	0x04
	ADDWF	FSR1L, F
	MOVLW	LOW(_rx_buf)
	ADDWF	r0x00, F
	MOVLW	HIGH(_rx_buf)
	ADDWFC	r0x01, F
	MOVFF	_RCREG, r0x02
	CLRF	r0x03
	MOVFF	r0x00, FSR0L
	MOVFF	r0x01, FSR0H
	MOVFF	r0x02, POSTINC0
	MOVFF	r0x03, INDF0
	BANKSEL	_rx_next
;	.line	158; main.c	inc(rx_next);
	INCFSZ	_rx_next, F, B
	BRA	_40298_DS_
	BANKSEL	(_rx_next + 1)
	INCF	(_rx_next + 1), F, B
_40298_DS_:
	BANKSEL	_rx_next
	BCF	_rx_next, 7, B
	BANKSEL	(_rx_next + 1)
	CLRF	(_rx_next + 1), B
;	.line	160; main.c	RX_flag = 0;
	BCF	_PIR1bits, 5
	MOVFF	PREINC1, r0x03
	MOVFF	PREINC1, r0x02
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_main__TMR0_isr	code
_TMR0_isr:
;	.line	107; main.c	void TMR0_isr (void)
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
;	.line	109; main.c	TMR0_ini = 53536;
	MOVLW	0x20
	BANKSEL	_TMR0_ini
	MOVWF	_TMR0_ini, B
	MOVLW	0xd1
	BANKSEL	(_TMR0_ini + 1)
	MOVWF	(_TMR0_ini + 1), B
	BANKSEL	_milisec
;	.line	110; main.c	if (milisec == 1000){SERVO_0 = 1 - SERVO_0; milisec = 0;}
	MOVF	_milisec, W, B
	XORLW	0xe8
	BNZ	_00119_DS_
	BANKSEL	(_milisec + 1)
	MOVF	(_milisec + 1), W, B
	XORLW	0x03
	BZ	_00120_DS_
_00119_DS_:
	BRA	_00113_DS_
_00120_DS_:
	CLRF	r0x00
	BTFSC	_LATBbits, 0
	INCF	r0x00, F
	CLRF	r0x01
	MOVF	r0x00, W
	SUBLW	0x01
	MOVWF	r0x00
	MOVLW	0x00
	SUBFWB	r0x01, F
	MOVF	r0x00, W
	ANDLW	0x01
	MOVWF	PRODH
	MOVF	_LATBbits, W
	ANDLW	0xfe
	IORWF	PRODH, W
	MOVWF	_LATBbits
	BANKSEL	_milisec
	CLRF	_milisec, B
	BANKSEL	(_milisec + 1)
	CLRF	(_milisec + 1), B
_00113_DS_:
	BANKSEL	_milisec
;	.line	111; main.c	milisec++;
	INCFSZ	_milisec, F, B
	BRA	_50299_DS_
	BANKSEL	(_milisec + 1)
	INCF	(_milisec + 1), F, B
_50299_DS_:
;	.line	149; main.c	set_TMR0 (TMR0_ini);
	MOVLW	0xd1
	MOVWF	_TMR0H
	MOVLW	0x20
	MOVWF	_TMR0L
;	.line	150; main.c	TMR0_flag = 0;
	BCF	_INTCONbits, 2
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_main__high_ISR	code
_high_ISR:
;	.line	86; main.c	void high_ISR (void) __interrupt 1
	MOVFF	STATUS, POSTDEC1
	MOVFF	BSR, POSTDEC1
	MOVWF	POSTDEC1
	MOVFF	PRODL, POSTDEC1
	MOVFF	PRODH, POSTDEC1
	MOVFF	FSR0L, POSTDEC1
	MOVFF	FSR0H, POSTDEC1
	MOVFF	PCLATH, POSTDEC1
	MOVFF	PCLATU, POSTDEC1
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
;	.line	99; main.c	if (TMR0_flag)
	BTFSS	_INTCONbits, 2
	BRA	_00107_DS_
;	.line	101; main.c	TMR0_isr ();
	CALL	_TMR0_isr
_00107_DS_:
	MOVFF	PREINC1, FSR2L
	MOVFF	PREINC1, PCLATU
	MOVFF	PREINC1, PCLATH
	MOVFF	PREINC1, FSR0H
	MOVFF	PREINC1, FSR0L
	MOVFF	PREINC1, PRODH
	MOVFF	PREINC1, PRODL
	MOVF	PREINC1, W
	MOVFF	PREINC1, BSR
	MOVFF	PREINC1, STATUS
	RETFIE	



; Statistics:
; code size:	 1514 (0x05ea) bytes ( 1.16%)
;           	  757 (0x02f5) words
; udata size:	  514 (0x0202) bytes (28.68%)
; access size:	    8 (0x0008) bytes


	end
