/*!
 *  \file
 *  \author Tibor Goldschwendt (<goldschwendt@cip.ifi.lmu.de>)
 */

#ifndef CDP_CDPP_TRANSFORMATIONITEM
#define CDP_CDPP_TRANSFORMATIONITEM

#include <vector>
#include "ModificationItem.h"

//#include "CDPPLib/Objects/Objects.h"

namespace cdp { namespace cdpp {
    
    /*! \addtogroup CDP_CDPP_MODIFICATIONITEMS
     *  @{
     */


    class TransformationItem : public ModificationItem {
        
    public:
		    // typedef Matrix<float, 4, 4> TransformationMatrix;
		    typedef int TransformationMatrix;
    protected:
        struct Core {
	  TransformationMatrix transformationMatrix;
        };
        
    private:
        Core _core;
        
    protected:
        const Core& core;
        
    public:
        TransformationItem (const TransformationMatrix transformationMatrix);
        TransformationItem ();
        // explicit TransformationItem (Deserialiser& deserialiser);    // Constructor for parsing
        
        virtual void serialise (SerDes& serDes);
        
        // Getter/Setter
        virtual size_t getSize () const;
        virtual void setTransformationMatrix (const TransformationMatrix transformationMatrix);
        virtual const TransformationMatrix getTransformationMatrix () const;
        
        // typedef boost::shared_ptr<TransformationItem> Ptr;

	ModificationItemField::TypeEnum getType () const {	return ModificationItemType::Position; }
    };
    /*! @} */
} } // cdp::cdpp

#endif /* defined(CDP_CDPP_ROTATIONITEM) */

