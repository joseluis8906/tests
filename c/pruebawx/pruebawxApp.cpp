/***************************************************************
 * Name:      pruebawxApp.cpp
 * Purpose:   Code for Application Class
 * Author:    jose caceres (joseluis8906@opmbx.org)
 * Created:   2016-09-01
 * Copyright: jose caceres (nd)
 * License:
 **************************************************************/

#ifdef WX_PRECOMP
#include "wx_pch.h"
#endif

#ifdef __BORLANDC__
#pragma hdrstop
#endif //__BORLANDC__

#include "pruebawxApp.h"
#include "pruebawxMain.h"

IMPLEMENT_APP(pruebawxApp);

bool pruebawxApp::OnInit()
{
    pruebawxFrame* frame = new pruebawxFrame(0L, _("wxWidgets Application Template"));
    
    frame->Show();
    
    return true;
}
