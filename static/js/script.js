// const confirmdelete =( id)=>{

// }

function confirmDelete(id){
    Swal.fire({
      title: 'info',
      title:'item deleted',
      showConfirmButton:true,
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Yes, delete it!"
      

   
}).then((result)=> {

  if (result.isConfirmed){
    window.location.href = `/delete-product/${id}`

  }
})
}