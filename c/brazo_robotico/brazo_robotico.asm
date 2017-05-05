;--------------------------------------------------------
; File Created by SDCC : free open source ANSI-C Compiler
; Version 3.5.0 #9253 (Jun 20 2015) (Linux)
; This file was generated Sat Jun 18 09:07:58 2016
;--------------------------------------------------------
; PIC16 port for the Microchip 16-bit core micros
;--------------------------------------------------------

	.ident "SDCC version 3.5.0 #9253 [pic16 port]"
	.file	"brazo_robotico.c"
	list	p=18f4550
	radix	dec
	CONFIG	PLLDIV=5
	CONFIG	FOSC=HSPLL_HS
	CONFIG	CPUDIV=OSC1_PLL2
	CONFIG	USBDIV=2
	CONFIG	WDT=OFF
	CONFIG	LVP=OFF
	CONFIG	PBADEN=OFF
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
	global	_setServoPosition
	global	_setElapsedTm
	global	_tmr0Isr
	global	_rxIsr
	global	_txIsr
	global	__putc
	global	_puts
	global	_getCh
	global	_setupUART
	global	_mover
	global	_servoActive
	global	_servoPosition
	global	_tmr0Ini
	global	_elapsedTm
	global	_led0counter
	global	_txBuf
	global	_txNext
	global	_txSend
	global	_rxBuf
	global	_rxNext
	global	_rxRead
	global	_ch
	global	_highIsr
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
PCL	equ	0xff9
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
_servoActive	db	0x00, 0x00
_servoPosition	db	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
_tmr0Ini	db	0x01, 0x00
_elapsedTm	db	0x00, 0x00
_led0counter	db	0x00, 0x00
_txNext	db	0x00, 0x00
_txSend	db	0x00, 0x00
_rxNext	db	0x00, 0x00
_rxRead	db	0x00, 0x00


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

udata_brazo_robotico_0	udata
_rxBuf	res	256

udata_brazo_robotico_1	udata
_txBuf	res	256

udata_brazo_robotico_2	udata
_ch	res	1

;--------------------------------------------------------
; interrupt vector
;--------------------------------------------------------

;--------------------------------------------------------
; global & static initialisations
;--------------------------------------------------------
; ; Starting pCode block for absolute section
; ;-----------------------------------------
S_brazo_robotico_ivec_0x1_highIsr	code	0X000008
ivec_0x1_highIsr:
	GOTO	_highIsr

; I code from now on!
; ; Starting pCode block
S_brazo_robotico__main	code
_main:
	.line	408; brazo_robotico.c	enable_global_ints;
	BSF	_INTCONbits, 7
	.line	412; brazo_robotico.c	enable_TMR0_int;
	BSF	_INTCONbits, 5
	.line	414; brazo_robotico.c	tmr0Ini = 5535;
	MOVLW	0x9f
	BANKSEL	_tmr0Ini
	MOVWF	_tmr0Ini, B
	MOVLW	0x15
	BANKSEL	(_tmr0Ini + 1)
	MOVWF	(_tmr0Ini + 1), B
	.line	415; brazo_robotico.c	setTmr0(tmr0Ini);
	MOVLW	0x15
	MOVWF	_TMR0H
	MOVLW	0x9e
	MOVWF	_TMR0L
	.line	417; brazo_robotico.c	T0CONbits.TMR0ON = 1;
	BSF	_T0CONbits, 7
	.line	418; brazo_robotico.c	T0CONbits.T08BIT = 0;
	BCF	_T0CONbits, 6
	.line	419; brazo_robotico.c	T0CONbits.T0CS = 0;
	BCF	_T0CONbits, 5
	.line	420; brazo_robotico.c	T0CONbits.T0SE = 0;
	BCF	_T0CONbits, 4
	.line	421; brazo_robotico.c	T0CONbits.PSA = 0;
	BCF	_T0CONbits, 3
	.line	422; brazo_robotico.c	T0CONbits.T0PS2 = 0;
	BCF	_T0CONbits, 2
	.line	423; brazo_robotico.c	T0CONbits.T0PS1 = 0;
	BCF	_T0CONbits, 1
	.line	424; brazo_robotico.c	T0CONbits.T0PS0 = 1;
	BSF	_T0CONbits, 0
	.line	428; brazo_robotico.c	TRISA = 0;
	CLRF	_TRISA
	.line	429; brazo_robotico.c	PORTA = 0;	
	CLRF	_PORTA
	.line	430; brazo_robotico.c	TRISB = 0;
	CLRF	_TRISB
	.line	431; brazo_robotico.c	PORTB = 0;
	CLRF	_PORTB
	.line	432; brazo_robotico.c	TRISC = 0;
	CLRF	_TRISC
	.line	433; brazo_robotico.c	PORTC = 0;
	CLRF	_PORTC
	.line	434; brazo_robotico.c	TRISD = 0;
	CLRF	_TRISD
	.line	435; brazo_robotico.c	PORTD = 0;
	CLRF	_PORTD
	.line	439; brazo_robotico.c	enable_RX_int;
	BSF	_PIE1bits, 5
	.line	441; brazo_robotico.c	setupUART ();
	CALL	_setupUART
_00349_DS_:
	.line	444; brazo_robotico.c	while (1)
	BRA	_00349_DS_
	RETURN	

; ; Starting pCode block
S_brazo_robotico__mover	code
_mover:
	.line	317; brazo_robotico.c	void mover (void)
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	.line	319; brazo_robotico.c	ch = getCh();
	CALL	_getCh
	BANKSEL	_ch
	MOVWF	_ch, B
	BANKSEL	_ch
	.line	321; brazo_robotico.c	if (ch == 'a')
	MOVF	_ch, W, B
	XORLW	0x61
	BNZ	_00215_DS_
	.line	323; brazo_robotico.c	if (servoPosition[0] > -4)
	MOVFF	_servoPosition, r0x00
	MOVFF	(_servoPosition + 1), r0x01
	MOVF	r0x01, W
	ADDLW	0x80
	ADDLW	0x81
	BNZ	_00316_DS_
	MOVLW	0xfd
	SUBWF	r0x00, W
_00316_DS_:
	BNC	_00215_DS_
	.line	325; brazo_robotico.c	servoPosition[0]--;
	MOVLW	0xff
	ADDWF	r0x00, F
	ADDWFC	r0x01, F
	MOVF	r0x00, W
	BANKSEL	_servoPosition
	MOVWF	_servoPosition, B
	MOVF	r0x01, W
	BANKSEL	(_servoPosition + 1)
	MOVWF	(_servoPosition + 1), B
_00215_DS_:
	BANKSEL	_ch
	.line	329; brazo_robotico.c	if (ch == 'b')
	MOVF	_ch, W, B
	XORLW	0x62
	BNZ	_00219_DS_
	.line	331; brazo_robotico.c	if (servoPosition[0] < 4)
	MOVFF	_servoPosition, r0x00
	MOVFF	(_servoPosition + 1), r0x01
	MOVF	r0x01, W
	ADDLW	0x80
	ADDLW	0x80
	BNZ	_00319_DS_
	MOVLW	0x04
	SUBWF	r0x00, W
_00319_DS_:
	BC	_00219_DS_
	.line	333; brazo_robotico.c	servoPosition[0]++;
	INFSNZ	r0x00, F
	INCF	r0x01, F
	MOVF	r0x00, W
	BANKSEL	_servoPosition
	MOVWF	_servoPosition, B
	MOVF	r0x01, W
	BANKSEL	(_servoPosition + 1)
	MOVWF	(_servoPosition + 1), B
_00219_DS_:
	BANKSEL	_ch
	.line	337; brazo_robotico.c	if (ch == 'c')
	MOVF	_ch, W, B
	XORLW	0x63
	BNZ	_00223_DS_
	.line	339; brazo_robotico.c	if (servoPosition[1] > -4)
	MOVFF	(_servoPosition + 2), r0x00
	MOVFF	(_servoPosition + 3), r0x01
	MOVF	r0x01, W
	ADDLW	0x80
	ADDLW	0x81
	BNZ	_00322_DS_
	MOVLW	0xfd
	SUBWF	r0x00, W
_00322_DS_:
	BNC	_00223_DS_
	.line	341; brazo_robotico.c	servoPosition[1]--;
	MOVLW	0xff
	ADDWF	r0x00, F
	ADDWFC	r0x01, F
	MOVF	r0x00, W
	BANKSEL	(_servoPosition + 2)
	MOVWF	(_servoPosition + 2), B
	MOVF	r0x01, W
	BANKSEL	(_servoPosition + 3)
	MOVWF	(_servoPosition + 3), B
_00223_DS_:
	BANKSEL	_ch
	.line	345; brazo_robotico.c	if (ch == 'd')
	MOVF	_ch, W, B
	XORLW	0x64
	BNZ	_00227_DS_
	.line	347; brazo_robotico.c	if (servoPosition[1] < 4)
	MOVFF	(_servoPosition + 2), r0x00
	MOVFF	(_servoPosition + 3), r0x01
	MOVF	r0x01, W
	ADDLW	0x80
	ADDLW	0x80
	BNZ	_00325_DS_
	MOVLW	0x04
	SUBWF	r0x00, W
_00325_DS_:
	BC	_00227_DS_
	.line	349; brazo_robotico.c	servoPosition[1]++;
	INFSNZ	r0x00, F
	INCF	r0x01, F
	MOVF	r0x00, W
	BANKSEL	(_servoPosition + 2)
	MOVWF	(_servoPosition + 2), B
	MOVF	r0x01, W
	BANKSEL	(_servoPosition + 3)
	MOVWF	(_servoPosition + 3), B
_00227_DS_:
	BANKSEL	_ch
	.line	353; brazo_robotico.c	if (ch == 'e')
	MOVF	_ch, W, B
	XORLW	0x65
	BNZ	_00231_DS_
	.line	355; brazo_robotico.c	if (servoPosition[2] > -4)
	MOVFF	(_servoPosition + 4), r0x00
	MOVFF	(_servoPosition + 5), r0x01
	MOVF	r0x01, W
	ADDLW	0x80
	ADDLW	0x81
	BNZ	_00328_DS_
	MOVLW	0xfd
	SUBWF	r0x00, W
_00328_DS_:
	BNC	_00231_DS_
	.line	357; brazo_robotico.c	servoPosition[2]--;
	MOVLW	0xff
	ADDWF	r0x00, F
	ADDWFC	r0x01, F
	MOVF	r0x00, W
	BANKSEL	(_servoPosition + 4)
	MOVWF	(_servoPosition + 4), B
	MOVF	r0x01, W
	BANKSEL	(_servoPosition + 5)
	MOVWF	(_servoPosition + 5), B
_00231_DS_:
	BANKSEL	_ch
	.line	361; brazo_robotico.c	if (ch == 'f')
	MOVF	_ch, W, B
	XORLW	0x66
	BNZ	_00235_DS_
	.line	363; brazo_robotico.c	if (servoPosition[2] < 4)
	MOVFF	(_servoPosition + 4), r0x00
	MOVFF	(_servoPosition + 5), r0x01
	MOVF	r0x01, W
	ADDLW	0x80
	ADDLW	0x80
	BNZ	_00331_DS_
	MOVLW	0x04
	SUBWF	r0x00, W
_00331_DS_:
	BC	_00235_DS_
	.line	365; brazo_robotico.c	servoPosition[2]++;
	INFSNZ	r0x00, F
	INCF	r0x01, F
	MOVF	r0x00, W
	BANKSEL	(_servoPosition + 4)
	MOVWF	(_servoPosition + 4), B
	MOVF	r0x01, W
	BANKSEL	(_servoPosition + 5)
	MOVWF	(_servoPosition + 5), B
_00235_DS_:
	BANKSEL	_ch
	.line	369; brazo_robotico.c	if (ch == 'g')
	MOVF	_ch, W, B
	XORLW	0x67
	BNZ	_00239_DS_
	.line	371; brazo_robotico.c	if (servoPosition[3] > -4)
	MOVFF	(_servoPosition + 6), r0x00
	MOVFF	(_servoPosition + 7), r0x01
	MOVF	r0x01, W
	ADDLW	0x80
	ADDLW	0x81
	BNZ	_00334_DS_
	MOVLW	0xfd
	SUBWF	r0x00, W
_00334_DS_:
	BNC	_00239_DS_
	.line	373; brazo_robotico.c	servoPosition[3]--;
	MOVLW	0xff
	ADDWF	r0x00, F
	ADDWFC	r0x01, F
	MOVF	r0x00, W
	BANKSEL	(_servoPosition + 6)
	MOVWF	(_servoPosition + 6), B
	MOVF	r0x01, W
	BANKSEL	(_servoPosition + 7)
	MOVWF	(_servoPosition + 7), B
_00239_DS_:
	BANKSEL	_ch
	.line	377; brazo_robotico.c	if (ch == 'h')
	MOVF	_ch, W, B
	XORLW	0x68
	BNZ	_00243_DS_
	.line	379; brazo_robotico.c	if (servoPosition[3] < 4)
	MOVFF	(_servoPosition + 6), r0x00
	MOVFF	(_servoPosition + 7), r0x01
	MOVF	r0x01, W
	ADDLW	0x80
	ADDLW	0x80
	BNZ	_00337_DS_
	MOVLW	0x04
	SUBWF	r0x00, W
_00337_DS_:
	BC	_00243_DS_
	.line	381; brazo_robotico.c	servoPosition[3]++;
	INFSNZ	r0x00, F
	INCF	r0x01, F
	MOVF	r0x00, W
	BANKSEL	(_servoPosition + 6)
	MOVWF	(_servoPosition + 6), B
	MOVF	r0x01, W
	BANKSEL	(_servoPosition + 7)
	MOVWF	(_servoPosition + 7), B
_00243_DS_:
	BANKSEL	_ch
	.line	385; brazo_robotico.c	if (ch == 'i')
	MOVF	_ch, W, B
	XORLW	0x69
	BNZ	_00247_DS_
	.line	387; brazo_robotico.c	if (servoPosition[4] > -4)
	MOVFF	(_servoPosition + 8), r0x00
	MOVFF	(_servoPosition + 9), r0x01
	MOVF	r0x01, W
	ADDLW	0x80
	ADDLW	0x81
	BNZ	_00340_DS_
	MOVLW	0xfd
	SUBWF	r0x00, W
_00340_DS_:
	BNC	_00247_DS_
	.line	389; brazo_robotico.c	servoPosition[4]--;
	MOVLW	0xff
	ADDWF	r0x00, F
	ADDWFC	r0x01, F
	MOVF	r0x00, W
	BANKSEL	(_servoPosition + 8)
	MOVWF	(_servoPosition + 8), B
	MOVF	r0x01, W
	BANKSEL	(_servoPosition + 9)
	MOVWF	(_servoPosition + 9), B
_00247_DS_:
	BANKSEL	_ch
	.line	393; brazo_robotico.c	if (ch == 'j')
	MOVF	_ch, W, B
	XORLW	0x6a
	BNZ	_00252_DS_
	.line	395; brazo_robotico.c	if (servoPosition[4] < 4)
	MOVFF	(_servoPosition + 8), r0x00
	MOVFF	(_servoPosition + 9), r0x01
	MOVF	r0x01, W
	ADDLW	0x80
	ADDLW	0x80
	BNZ	_00343_DS_
	MOVLW	0x04
	SUBWF	r0x00, W
_00343_DS_:
	BC	_00252_DS_
	.line	397; brazo_robotico.c	servoPosition[4]++;
	INFSNZ	r0x00, F
	INCF	r0x01, F
	MOVF	r0x00, W
	BANKSEL	(_servoPosition + 8)
	MOVWF	(_servoPosition + 8), B
	MOVF	r0x01, W
	BANKSEL	(_servoPosition + 9)
	MOVWF	(_servoPosition + 9), B
_00252_DS_:
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_brazo_robotico__setupUART	code
_setupUART:
	.line	298; brazo_robotico.c	void setupUART ()
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	.line	300; brazo_robotico.c	TRISCbits.TRISC6 = 1; 	//TX
	BSF	_TRISCbits, 6
	.line	301; brazo_robotico.c	TXSTAbits.TXEN = 1;	//transmisión habilitada
	BSF	_TXSTAbits, 5
	.line	302; brazo_robotico.c	TXSTAbits.SYNC = 0; 	//modo asíncrono
	BCF	_TXSTAbits, 4
	.line	303; brazo_robotico.c	TXSTAbits.BRGH = 0;	//velocidad de boud rate 0 baja velocidad 1 alta velocidad
	BCF	_TXSTAbits, 2
	.line	305; brazo_robotico.c	TRISCbits.TRISC7 = 1; 	//RX
	BSF	_TRISCbits, 7
	.line	306; brazo_robotico.c	RCSTAbits.SPEN = 1;	//habilitar el puerto serial
	BSF	_RCSTAbits, 7
	.line	307; brazo_robotico.c	RCSTAbits.CREN = 1;	//habilitar RX para recibir
	BSF	_RCSTAbits, 4
	.line	310; brazo_robotico.c	BAUDCONbits.BRG16 = 0; 	//16 bit baud rate desactivado
	BCF	_BAUDCONbits, 3
	.line	312; brazo_robotico.c	SPBRG = 77;
	MOVLW	0x4d
	MOVWF	_SPBRG
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_brazo_robotico__getCh	code
_getCh:
	.line	289; brazo_robotico.c	unsigned char getCh (void)
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	BANKSEL	(_rxRead + 1)
	.line	291; brazo_robotico.c	unsigned char ch = rxBuf[rxRead];
	MOVF	(_rxRead + 1), W, B
	MOVWF	POSTDEC1
	BANKSEL	_rxRead
	MOVF	_rxRead, W, B
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
	MOVLW	LOW(_rxBuf)
	ADDWF	r0x00, F
	MOVLW	HIGH(_rxBuf)
	ADDWFC	r0x01, F
	MOVFF	r0x00, FSR0L
	MOVFF	r0x01, FSR0H
	MOVFF	POSTINC0, r0x00
	MOVFF	INDF0, r0x01
	BANKSEL	_rxRead
	.line	292; brazo_robotico.c	inc(rxRead);
	INCFSZ	_rxRead, F, B
	BRA	_10348_DS_
	BANKSEL	(_rxRead + 1)
	INCF	(_rxRead + 1), F, B
_10348_DS_:
	BANKSEL	_rxRead
	BCF	_rxRead, 7, B
	BANKSEL	(_rxRead + 1)
	CLRF	(_rxRead + 1), B
	.line	293; brazo_robotico.c	return ch;
	MOVF	r0x00, W
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_brazo_robotico__puts	code
_puts:
	.line	275; brazo_robotico.c	void puts (const unsigned char ch[])
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
	.line	278; brazo_robotico.c	do
	CLRF	r0x03
	CLRF	r0x04
_00194_DS_:
	.line	280; brazo_robotico.c	_putc (ch[i]);
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
	.line	281; brazo_robotico.c	i++;
	INFSNZ	r0x03, F
	INCF	r0x04, F
	.line	283; brazo_robotico.c	while (ch[i] != '\0');
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
	BNZ	_00194_DS_
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
S_brazo_robotico___putc	code
__putc:
	.line	267; brazo_robotico.c	void _putc (unsigned char ch)
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	MOVFF	r0x02, POSTDEC1
	MOVFF	r0x03, POSTDEC1
	MOVLW	0x02
	MOVFF	PLUSW2, r0x00
	BANKSEL	(_txNext + 1)
	.line	269; brazo_robotico.c	txBuf[txNext]=ch;
	MOVF	(_txNext + 1), W, B
	MOVWF	POSTDEC1
	BANKSEL	_txNext
	MOVF	_txNext, W, B
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
	MOVLW	LOW(_txBuf)
	ADDWF	r0x01, F
	MOVLW	HIGH(_txBuf)
	ADDWFC	r0x02, F
	CLRF	r0x03
	MOVFF	r0x01, FSR0L
	MOVFF	r0x02, FSR0H
	MOVFF	r0x00, POSTINC0
	MOVFF	r0x03, INDF0
	BANKSEL	_txNext
	.line	270; brazo_robotico.c	inc(txNext);
	INCFSZ	_txNext, F, B
	BRA	_20349_DS_
	BANKSEL	(_txNext + 1)
	INCF	(_txNext + 1), F, B
_20349_DS_:
	BANKSEL	_txNext
	BCF	_txNext, 7, B
	BANKSEL	(_txNext + 1)
	CLRF	(_txNext + 1), B
	.line	271; brazo_robotico.c	enable_TX_int;
	BSF	_PIE1bits, 4
	MOVFF	PREINC1, r0x03
	MOVFF	PREINC1, r0x02
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_brazo_robotico__txIsr	code
_txIsr:
	.line	251; brazo_robotico.c	void txIsr (void)
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	BANKSEL	_txSend
	.line	253; brazo_robotico.c	if (txSend==txNext)
	MOVF	_txSend, W, B
	BANKSEL	_txNext
	XORWF	_txNext, W, B
	BNZ	_00183_DS_
	BANKSEL	(_txSend + 1)
	MOVF	(_txSend + 1), W, B
	BANKSEL	(_txNext + 1)
	XORWF	(_txNext + 1), W, B
	BZ	_00184_DS_
_00183_DS_:
	BRA	_00176_DS_
_00184_DS_:
	.line	255; brazo_robotico.c	disable_TX_int;
	BCF	_PIE1bits, 4
	BRA	_00177_DS_
_00176_DS_:
	BANKSEL	(_txSend + 1)
	.line	259; brazo_robotico.c	TXREG = txBuf[txSend];
	MOVF	(_txSend + 1), W, B
	MOVWF	POSTDEC1
	BANKSEL	_txSend
	MOVF	_txSend, W, B
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
	MOVLW	LOW(_txBuf)
	ADDWF	r0x00, F
	MOVLW	HIGH(_txBuf)
	ADDWFC	r0x01, F
	MOVFF	r0x00, FSR0L
	MOVFF	r0x01, FSR0H
	MOVFF	POSTINC0, r0x00
	MOVFF	INDF0, r0x01
	MOVF	r0x00, W
	MOVWF	_TXREG
	BANKSEL	_txSend
	.line	260; brazo_robotico.c	inc(txSend);
	INCFSZ	_txSend, F, B
	BRA	_30350_DS_
	BANKSEL	(_txSend + 1)
	INCF	(_txSend + 1), F, B
_30350_DS_:
	BANKSEL	_txSend
	BCF	_txSend, 7, B
	BANKSEL	(_txSend + 1)
	CLRF	(_txSend + 1), B
_00177_DS_:
	.line	262; brazo_robotico.c	TX_flag = 0;
	BCF	_PIR1bits, 4
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_brazo_robotico__rxIsr	code
_rxIsr:
	.line	240; brazo_robotico.c	void rxIsr (void) 
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	MOVFF	r0x02, POSTDEC1
	MOVFF	r0x03, POSTDEC1
	BANKSEL	(_rxNext + 1)
	.line	242; brazo_robotico.c	rxBuf[rxNext] = (unsigned char) RCREG;
	MOVF	(_rxNext + 1), W, B
	MOVWF	POSTDEC1
	BANKSEL	_rxNext
	MOVF	_rxNext, W, B
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
	MOVLW	LOW(_rxBuf)
	ADDWF	r0x00, F
	MOVLW	HIGH(_rxBuf)
	ADDWFC	r0x01, F
	MOVFF	_RCREG, r0x02
	CLRF	r0x03
	MOVFF	r0x00, FSR0L
	MOVFF	r0x01, FSR0H
	MOVFF	r0x02, POSTINC0
	MOVFF	r0x03, INDF0
	BANKSEL	_rxNext
	.line	243; brazo_robotico.c	inc(rxNext);
	INCFSZ	_rxNext, F, B
	BRA	_40351_DS_
	BANKSEL	(_rxNext + 1)
	INCF	(_rxNext + 1), F, B
_40351_DS_:
	BANKSEL	_rxNext
	BCF	_rxNext, 7, B
	BANKSEL	(_rxNext + 1)
	CLRF	(_rxNext + 1), B
	.line	245; brazo_robotico.c	mover ();
	CALL	_mover
	.line	246; brazo_robotico.c	RX_flag = 0;
	BCF	_PIR1bits, 5
	MOVFF	PREINC1, r0x03
	MOVFF	PREINC1, r0x02
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_brazo_robotico__tmr0Isr	code
_tmr0Isr:
	.line	162; brazo_robotico.c	void tmr0Isr (void)
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	MOVFF	r0x00, POSTDEC1
	MOVFF	r0x01, POSTDEC1
	BANKSEL	_led0counter
	.line	164; brazo_robotico.c	led0counter++;
	INCFSZ	_led0counter, F, B
	BRA	_50352_DS_
	BANKSEL	(_led0counter + 1)
	INCF	(_led0counter + 1), F, B
_50352_DS_:
	BANKSEL	(_led0counter + 1)
	.line	165; brazo_robotico.c	if (led0counter >= 240)
	MOVF	(_led0counter + 1), W, B
	ADDLW	0x80
	ADDLW	0x80
	BNZ	_00163_DS_
	MOVLW	0xf0
	BANKSEL	_led0counter
	SUBWF	_led0counter, W, B
_00163_DS_:
	BNC	_00147_DS_
	.line	167; brazo_robotico.c	PinD0 = 1 - PinD0;
	CLRF	r0x00
	BTFSC	_LATDbits, 0
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
	MOVF	_LATDbits, W
	ANDLW	0xfe
	IORWF	PRODH, W
	MOVWF	_LATDbits
	BANKSEL	_led0counter
	.line	168; brazo_robotico.c	led0counter = 0;
	CLRF	_led0counter, B
	BANKSEL	(_led0counter + 1)
	CLRF	(_led0counter + 1), B
_00147_DS_:
	.line	171; brazo_robotico.c	switch (servoActive)
	MOVLW	0x00
	BANKSEL	(_servoActive + 1)
	SUBWF	(_servoActive + 1), W, B
	BNZ	_00164_DS_
	MOVLW	0x06
	BANKSEL	_servoActive
	SUBWF	_servoActive, W, B
_00164_DS_:
	BTFSC	STATUS, 0
	BRA	_00154_DS_
	CLRF	PCLATH
	CLRF	PCLATU
	BANKSEL	_servoActive
	RLCF	_servoActive, W, B
	RLCF	PCLATH, F
	RLCF	WREG, W
	RLCF	PCLATH, F
	ANDLW	0xfc
	ADDLW	LOW(_00165_DS_)
	MOVWF	POSTDEC1
	MOVLW	HIGH(_00165_DS_)
	ADDWFC	PCLATH, F
	MOVLW	UPPER(_00165_DS_)
	ADDWFC	PCLATU, F
	MOVF	PREINC1, W
	MOVWF	PCL
_00165_DS_:
	GOTO	_00148_DS_
	GOTO	_00149_DS_
	GOTO	_00150_DS_
	GOTO	_00151_DS_
	GOTO	_00152_DS_
	GOTO	_00153_DS_
_00148_DS_:
	.line	174; brazo_robotico.c	servo0 = 1;
	BSF	_LATBbits, 0
	.line	175; brazo_robotico.c	servo1 = 0;
	BCF	_LATBbits, 1
	.line	176; brazo_robotico.c	servo2 = 0;
	BCF	_LATBbits, 2
	.line	177; brazo_robotico.c	servo3 = 0;
	BCF	_LATBbits, 3
	.line	178; brazo_robotico.c	servo4 = 0;
	BCF	_LATBbits, 4
	BANKSEL	_elapsedTm
	.line	179; brazo_robotico.c	elapsedTm = 0;
	CLRF	_elapsedTm, B
	BANKSEL	(_elapsedTm + 1)
	CLRF	(_elapsedTm + 1), B
	BANKSEL	(_servoPosition + 1)
	.line	180; brazo_robotico.c	setServoPosition(servoPosition[0]);
	MOVF	(_servoPosition + 1), W, B
	MOVWF	POSTDEC1
	BANKSEL	_servoPosition
	MOVF	_servoPosition, W, B
	MOVWF	POSTDEC1
	CALL	_setServoPosition
	MOVF	POSTINC1, F
	MOVF	POSTINC1, F
	BANKSEL	_servoActive
	.line	181; brazo_robotico.c	servoActive++;
	INCFSZ	_servoActive, F, B
	BRA	_60353_DS_
	BANKSEL	(_servoActive + 1)
	INCF	(_servoActive + 1), F, B
_60353_DS_:
	.line	182; brazo_robotico.c	break;
	BRA	_00154_DS_
_00149_DS_:
	.line	185; brazo_robotico.c	servo0 = 0;
	BCF	_LATBbits, 0
	.line	186; brazo_robotico.c	servo1 = 1;
	BSF	_LATBbits, 1
	.line	187; brazo_robotico.c	servo2 = 0;
	BCF	_LATBbits, 2
	.line	188; brazo_robotico.c	servo3 = 0;
	BCF	_LATBbits, 3
	.line	189; brazo_robotico.c	servo4 = 0;
	BCF	_LATBbits, 4
	BANKSEL	(_servoPosition + 3)
	.line	190; brazo_robotico.c	setServoPosition(servoPosition[1]);
	MOVF	(_servoPosition + 3), W, B
	MOVWF	POSTDEC1
	BANKSEL	(_servoPosition + 2)
	MOVF	(_servoPosition + 2), W, B
	MOVWF	POSTDEC1
	CALL	_setServoPosition
	MOVF	POSTINC1, F
	MOVF	POSTINC1, F
	BANKSEL	_servoActive
	.line	191; brazo_robotico.c	servoActive++;
	INCFSZ	_servoActive, F, B
	BRA	_70354_DS_
	BANKSEL	(_servoActive + 1)
	INCF	(_servoActive + 1), F, B
_70354_DS_:
	.line	192; brazo_robotico.c	break;
	BRA	_00154_DS_
_00150_DS_:
	.line	195; brazo_robotico.c	servo0 = 0;
	BCF	_LATBbits, 0
	.line	196; brazo_robotico.c	servo1 = 0;
	BCF	_LATBbits, 1
	.line	197; brazo_robotico.c	servo2 = 1;
	BSF	_LATBbits, 2
	.line	198; brazo_robotico.c	servo3 = 0;
	BCF	_LATBbits, 3
	.line	199; brazo_robotico.c	servo4 = 0;
	BCF	_LATBbits, 4
	BANKSEL	(_servoPosition + 5)
	.line	200; brazo_robotico.c	setServoPosition(servoPosition[2]);
	MOVF	(_servoPosition + 5), W, B
	MOVWF	POSTDEC1
	BANKSEL	(_servoPosition + 4)
	MOVF	(_servoPosition + 4), W, B
	MOVWF	POSTDEC1
	CALL	_setServoPosition
	MOVF	POSTINC1, F
	MOVF	POSTINC1, F
	BANKSEL	_servoActive
	.line	201; brazo_robotico.c	servoActive++;
	INCFSZ	_servoActive, F, B
	BRA	_80355_DS_
	BANKSEL	(_servoActive + 1)
	INCF	(_servoActive + 1), F, B
_80355_DS_:
	.line	202; brazo_robotico.c	break;
	BRA	_00154_DS_
_00151_DS_:
	.line	205; brazo_robotico.c	servo0 = 0;
	BCF	_LATBbits, 0
	.line	206; brazo_robotico.c	servo1 = 0;
	BCF	_LATBbits, 1
	.line	207; brazo_robotico.c	servo2 = 0;
	BCF	_LATBbits, 2
	.line	208; brazo_robotico.c	servo3 = 1;
	BSF	_LATBbits, 3
	.line	209; brazo_robotico.c	servo4 = 0;
	BCF	_LATBbits, 4
	BANKSEL	(_servoPosition + 7)
	.line	210; brazo_robotico.c	setServoPosition(servoPosition[3]);
	MOVF	(_servoPosition + 7), W, B
	MOVWF	POSTDEC1
	BANKSEL	(_servoPosition + 6)
	MOVF	(_servoPosition + 6), W, B
	MOVWF	POSTDEC1
	CALL	_setServoPosition
	MOVF	POSTINC1, F
	MOVF	POSTINC1, F
	BANKSEL	_servoActive
	.line	211; brazo_robotico.c	servoActive++;
	INCFSZ	_servoActive, F, B
	BRA	_90356_DS_
	BANKSEL	(_servoActive + 1)
	INCF	(_servoActive + 1), F, B
_90356_DS_:
	.line	212; brazo_robotico.c	break;
	BRA	_00154_DS_
_00152_DS_:
	.line	215; brazo_robotico.c	servo0 = 0;
	BCF	_LATBbits, 0
	.line	216; brazo_robotico.c	servo1 = 0;
	BCF	_LATBbits, 1
	.line	217; brazo_robotico.c	servo2 = 0;
	BCF	_LATBbits, 2
	.line	218; brazo_robotico.c	servo3 = 0;
	BCF	_LATBbits, 3
	.line	219; brazo_robotico.c	servo4 = 1;
	BSF	_LATBbits, 4
	BANKSEL	(_servoPosition + 9)
	.line	220; brazo_robotico.c	setServoPosition(servoPosition[4]);
	MOVF	(_servoPosition + 9), W, B
	MOVWF	POSTDEC1
	BANKSEL	(_servoPosition + 8)
	MOVF	(_servoPosition + 8), W, B
	MOVWF	POSTDEC1
	CALL	_setServoPosition
	MOVF	POSTINC1, F
	MOVF	POSTINC1, F
	BANKSEL	_servoActive
	.line	221; brazo_robotico.c	servoActive++;
	INCFSZ	_servoActive, F, B
	BRA	_100357_DS_
	BANKSEL	(_servoActive + 1)
	INCF	(_servoActive + 1), F, B
_100357_DS_:
	.line	222; brazo_robotico.c	break;
	BRA	_00154_DS_
_00153_DS_:
	.line	225; brazo_robotico.c	servo0 = 0;
	BCF	_LATBbits, 0
	.line	226; brazo_robotico.c	servo1 = 0;
	BCF	_LATBbits, 1
	.line	227; brazo_robotico.c	servo2 = 0;
	BCF	_LATBbits, 2
	.line	228; brazo_robotico.c	servo3 = 0;
	BCF	_LATBbits, 3
	.line	229; brazo_robotico.c	servo4 = 0;
	BCF	_LATBbits, 4
	.line	230; brazo_robotico.c	setElapsedTm ();
	CALL	_setElapsedTm
	BANKSEL	_servoActive
	.line	231; brazo_robotico.c	servoActive=0;
	CLRF	_servoActive, B
	BANKSEL	(_servoActive + 1)
	CLRF	(_servoActive + 1), B
_00154_DS_:
	BANKSEL	_tmr0Ini
	.line	234; brazo_robotico.c	setTmr0(tmr0Ini);
	MOVF	_tmr0Ini, W, B
	ADDLW	0xff
	MOVWF	r0x00
	MOVLW	0xff
	BANKSEL	(_tmr0Ini + 1)
	ADDWFC	(_tmr0Ini + 1), W, B
	MOVWF	r0x01
	MOVF	r0x01, W
	MOVWF	r0x00
	CLRF	r0x01
	MOVF	r0x00, W
	MOVWF	_TMR0H
	BANKSEL	_tmr0Ini
	MOVF	_tmr0Ini, W, B
	MOVWF	r0x00
	DECF	r0x00, W
	MOVWF	_TMR0L
	.line	236; brazo_robotico.c	TMR0_flag = 0;
	BCF	_INTCONbits, 2
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_brazo_robotico__setElapsedTm	code
_setElapsedTm:
	.line	156; brazo_robotico.c	void setElapsedTm (void)
	MOVFF	FSR2L, POSTDEC1
	MOVFF	FSR1L, FSR2L
	BANKSEL	_elapsedTm
	.line	158; brazo_robotico.c	tmr0Ini = elapsedTm+5535;
	MOVF	_elapsedTm, W, B
	ADDLW	0x9f
	BANKSEL	_tmr0Ini
	MOVWF	_tmr0Ini, B
	MOVLW	0x15
	BANKSEL	(_elapsedTm + 1)
	ADDWFC	(_elapsedTm + 1), W, B
	BANKSEL	(_tmr0Ini + 1)
	MOVWF	(_tmr0Ini + 1), B
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_brazo_robotico__setServoPosition	code
_setServoPosition:
	.line	125; brazo_robotico.c	void setServoPosition (int position)
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
	.line	127; brazo_robotico.c	unsigned int cl = 1500;
	MOVLW	0xdc
	MOVWF	r0x02
	MOVLW	0x05
	MOVWF	r0x03
	.line	129; brazo_robotico.c	switch (position)
	MOVF	r0x01, W
	ADDLW	0x80
	ADDLW	0x81
	BNZ	_00134_DS_
	MOVLW	0xfc
	SUBWF	r0x00, W
_00134_DS_:
	BTFSS	STATUS, 0
	BRA	_00125_DS_
	MOVF	r0x01, W
	ADDLW	0x80
	ADDLW	0x80
	BNZ	_00135_DS_
	MOVLW	0x05
	SUBWF	r0x00, W
_00135_DS_:
	BTFSC	STATUS, 0
	BRA	_00125_DS_
	MOVLW	0x04
	ADDWF	r0x00, F
	CLRF	PCLATH
	CLRF	PCLATU
	RLCF	r0x00, W
	RLCF	PCLATH, F
	RLCF	WREG, W
	RLCF	PCLATH, F
	ANDLW	0xfc
	ADDLW	LOW(_00136_DS_)
	MOVWF	POSTDEC1
	MOVLW	HIGH(_00136_DS_)
	ADDWFC	PCLATH, F
	MOVLW	UPPER(_00136_DS_)
	ADDWFC	PCLATU, F
	MOVF	PREINC1, W
	MOVWF	PCL
_00136_DS_:
	GOTO	_00116_DS_
	GOTO	_00117_DS_
	GOTO	_00118_DS_
	GOTO	_00119_DS_
	GOTO	_00120_DS_
	GOTO	_00121_DS_
	GOTO	_00122_DS_
	GOTO	_00123_DS_
	GOTO	_00124_DS_
_00116_DS_:
	.line	131; brazo_robotico.c	case -4: cl = 1450; break;
	MOVLW	0xaa
	MOVWF	r0x02
	MOVLW	0x05
	MOVWF	r0x03
	BRA	_00125_DS_
_00117_DS_:
	.line	133; brazo_robotico.c	case -3: cl = 2087; break;
	MOVLW	0x27
	MOVWF	r0x02
	MOVLW	0x08
	MOVWF	r0x03
	BRA	_00125_DS_
_00118_DS_:
	.line	135; brazo_robotico.c	case -2: cl = 2725; break;
	MOVLW	0xa5
	MOVWF	r0x02
	MOVLW	0x0a
	MOVWF	r0x03
	BRA	_00125_DS_
_00119_DS_:
	.line	137; brazo_robotico.c	case -1: cl = 3362; break;
	MOVLW	0x22
	MOVWF	r0x02
	MOVLW	0x0d
	MOVWF	r0x03
	BRA	_00125_DS_
_00120_DS_:
	.line	139; brazo_robotico.c	case 0: cl = 4000; break;
	MOVLW	0xa0
	MOVWF	r0x02
	MOVLW	0x0f
	MOVWF	r0x03
	BRA	_00125_DS_
_00121_DS_:
	.line	141; brazo_robotico.c	case 1: cl = 4900; break;
	MOVLW	0x24
	MOVWF	r0x02
	MOVLW	0x13
	MOVWF	r0x03
	BRA	_00125_DS_
_00122_DS_:
	.line	143; brazo_robotico.c	case 2: cl = 5700; break;
	MOVLW	0x44
	MOVWF	r0x02
	MOVLW	0x16
	MOVWF	r0x03
	BRA	_00125_DS_
_00123_DS_:
	.line	145; brazo_robotico.c	case 3: cl = 6500; break;
	MOVLW	0x64
	MOVWF	r0x02
	MOVLW	0x19
	MOVWF	r0x03
	BRA	_00125_DS_
_00124_DS_:
	.line	147; brazo_robotico.c	case 4: cl = 7300; break;
	MOVLW	0x84
	MOVWF	r0x02
	MOVLW	0x1c
	MOVWF	r0x03
_00125_DS_:
	.line	150; brazo_robotico.c	elapsedTm = elapsedTm+cl;
	MOVF	r0x02, W
	BANKSEL	_elapsedTm
	ADDWF	_elapsedTm, F, B
	MOVF	r0x03, W
	BANKSEL	(_elapsedTm + 1)
	ADDWFC	(_elapsedTm + 1), F, B
	.line	152; brazo_robotico.c	tmr0Ini = 65535-cl;
	CLRF	r0x00
	CLRF	r0x01
	MOVF	r0x02, W
	SUBLW	0xff
	MOVWF	r0x02
	MOVLW	0xff
	SUBFWB	r0x03, F
	MOVLW	0x00
	SUBFWB	r0x00, F
	MOVLW	0x00
	SUBFWB	r0x01, F
	MOVF	r0x02, W
	BANKSEL	_tmr0Ini
	MOVWF	_tmr0Ini, B
	MOVF	r0x03, W
	BANKSEL	(_tmr0Ini + 1)
	MOVWF	(_tmr0Ini + 1), B
	MOVFF	PREINC1, r0x03
	MOVFF	PREINC1, r0x02
	MOVFF	PREINC1, r0x01
	MOVFF	PREINC1, r0x00
	MOVFF	PREINC1, FSR2L
	RETURN	

; ; Starting pCode block
S_brazo_robotico__highIsr	code
_highIsr:
	.line	105; brazo_robotico.c	void highIsr (void) __interrupt 1
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
	.line	107; brazo_robotico.c	if (RX_flag)
	BTFSS	_PIR1bits, 5
	BRA	_00106_DS_
	.line	109; brazo_robotico.c	rxIsr ();
	CALL	_rxIsr
_00106_DS_:
	.line	112; brazo_robotico.c	if (TX_flag)
	BTFSS	_PIR1bits, 4
	BRA	_00108_DS_
	.line	114; brazo_robotico.c	txIsr ();
	CALL	_txIsr
_00108_DS_:
	.line	117; brazo_robotico.c	if (TMR0_flag)
	BTFSS	_INTCONbits, 2
	BRA	_00111_DS_
	.line	119; brazo_robotico.c	tmr0Isr ();
	CALL	_tmr0Isr
_00111_DS_:
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
; code size:	 2208 (0x08a0) bytes ( 1.68%)
;           	 1104 (0x0450) words
; udata size:	  513 (0x0201) bytes (28.63%)
; access size:	    8 (0x0008) bytes


	end
