/*!
 *  \file
 *  \author Tibor Goldschwendt (<goldschwendt@cip.ifi.lmu.de>)
 */

// #include "CDPPLib/Exceptions/Exceptions.h"
#include "TransformationItem.h"


using namespace cdp::cdpp;

TransformationItem::TransformationItem (const TransformationMatrix transformationMatrix) : core(_core) {
    
    this->_core.transformationMatrix = transformationMatrix;
}

TransformationItem::TransformationItem () : core(_core) {
    
  this->_core.transformationMatrix = 6;
}

//TransformationItem::TransformationItem (Deserialiser& deserialiser) : core(_core) {
//  this->serialise(deserialiser);
//}

void TransformationItem::serialise (SerDes& serDes) {
    
  //ModificationItem::serialise(serDes);
    
  //  serDes & this->_core.transformationMatrix;
}

size_t TransformationItem::getSize () const {
    
  return ModificationItem::getSize() + 4; // TransformationMatrix::getSize();
}

void TransformationItem::setTransformationMatrix (const TransformationMatrix transformationMatrix) {
    this->_core.transformationMatrix = transformationMatrix;
}

const TransformationItem::TransformationMatrix TransformationItem::getTransformationMatrix () const {
    return this->core.transformationMatrix;
}
