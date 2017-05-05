/***************************************************************
 * Name:      pruebawxMain.h
 * Purpose:   Defines Application Frame
 * Author:    jose caceres (joseluis8906@opmbx.org)
 * Created:   2016-09-01
 * Copyright: jose caceres (nd)
 * License:
 **************************************************************/

#ifndef PRUEBAWXMAIN_H
#define PRUEBAWXMAIN_H

#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include "pruebawxApp.h"

class pruebawxFrame: public wxFrame
{
    public:
        pruebawxFrame(wxFrame *frame, const wxString& title);
        ~pruebawxFrame();
    private:
        enum
        {
            idMenuQuit = 1000,
            idMenuAbout
        };
        void OnClose(wxCloseEvent& event);
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        DECLARE_EVENT_TABLE()
};


#endif // PRUEBAWXMAIN_H
