function fetchAndDisplayUsers() { // สร้าง Function
        // ดึงข้อมูล API จากเว็ป jsonplaceholder ในหัวข้อ users , เรียกว่าการ Get Reqest เพื่อขอข้อมูลจากเว็ป
    fetch("https://jsonplaceholder.typicode.com/users") // ข้อมูลในเว็ปจะเป็น string
    .then(response => { // กำหนดข้อมูลเป็น response
        if (!response.ok) {
            throw new Error("Network response was not ok" + response.statusText); // หากตัวแปร response ไม่โอเค จะแสดงข้อความ Network response was not ok
        }
        return response.json(); // หากตัวแปร response ok ก็จะทำการแปลงข้อมูลเป็น(JS object) โดยใช้ json method เพื่อให้สามารถใช้ในแอพของเราได้
    })
    .then(data => { // เราได้ข้อมูลจริงๆ จากการแปลงข้อมูลเป็น JS object , กำหนด Object = data
        console.log(data); // log ข้อมูลออกทาง console
        const userContainer = document.getElementById("users-Container"); // get tag div มา
        userContainer.innerHTML = ""; // Clear any existing content

        data.forEach(user => { // รับค่าข้อมูลมา 1 ตัว
            const userDiv = document.createElement("div") // คล้ายๆว่าเราสร้าง tag div มาอีกตัวใน tag div อีกที
            userDiv.innerHTML = `
                <h2> ${user.name} </h2> 
                <p><strong>Email :</strong> ${user.email} </p>
                <p><strong>phone :</strong> ${user.phone} </p>
                <p><strong>website :</strong> ${user.website} </p>
                <p><strong>address :</strong> ${user.address.city}, <strong>ZipCode :</strong> ${user.address.zipcode} </p>
                <p><strong>website :</strong> ${user.website} </p>
            `; // เราสามารระบุข้อมูลที่เราต้องการแสดงได้

            userContainer.appendChild(userDiv); // การเอา userDiv ไปแสดงใน userContainer
        })
    })
    .catch(error => { // รับ parmitor error มา
        console.error("There was a problem with the fetch operation", error);
    });
}

fetchAndDisplayUsers(); // เรียกใช้ Function

