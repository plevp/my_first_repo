/*!
 *  \file
 *  \author Tibor Goldschwendt (<goldschwendt@cip.ifi.lmu.de>)
 */

#ifndef CDPPLib_MessageDefinitions_h
#define CDPPLib_MessageDefinitions_h

// Types and constants used in CDPP messages.

namespace cdp { namespace cdpp {
    
    /*! \addtogroup CDP_CDPP_MESSAGES
     * @{   
     */
    // Types of messages.
    namespace MessageType {
        
        enum MessageType {
            // Control messages
            SignInMessage           = 0,
            WelcomeMessage          = 1,
            LogOutMessage           = 2,
            ReadyForUpdateMessage   = 3,
            RequestReloadMessage    = 4,
            ErrorMessage            = 5,
            WarningMessage          = 6,
            RegisterPluginMessage   = 7,
            // Update message
            UpdateMessage           = 8,
            // Scene message
            SceneMessage            = 9,
        };
    }
    /*! @} */
    
} } // cdp::cdpp

#endif
