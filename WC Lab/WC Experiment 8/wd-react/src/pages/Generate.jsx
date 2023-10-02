import React from 'react'

const Generate = (prop) => {
  return (
    <div className='center p-20 text-2xl'>
      This <span className='font-bold text-blue-600'>{prop.data}</span> has been recieved from sidebar.
    </div>
  )
}

export default Generate
