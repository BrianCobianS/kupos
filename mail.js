const nodemailer = require("nodemailer");
const datos= {  
    msg: 'Aun no cambia la agenada',
    email: 'brian.cobian@alumnos.udg.mx',

} 

const Enviarmail= async (datos)=>{
	let transporter = nodemailer.createTransport({
        host: "smtp.gmail.com",
        port: 465,
        secure: true, // true for 465, false for other ports
        auth: {
          user: 'unattendedinstallation@gmail.com', // generated ethereal user
          pass: 'lxcyphalpqqvhuvi', // generated ethereal password
        },
    });
	const{ email, msg} = datos
    console.log(email)
    const info = await transporter.sendMail({
        from:  "API - Unattended Intallation",
        to: email,
        subject: `${msg}`,
        text: `${msg}`,
        
    })
    console.log("Mensaje enviado: %s", info.messageId)
}
Enviarmail(datos)