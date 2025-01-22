$(document).ready(function () {


    $('#uploadForm').on('submit', function (e) {
        e.preventDefault();
        
        // FormData 객체 생성
        const formData = new FormData();
        
        // 파일과 이름 가져오기
        const imageFile = $('#imageInput')[0].files[0];


        // 유효성 검사
        if (!imageFile) {
            alert("이미지 파일을 선택해주세요.");
            return;
        }




        // FormData에 데이터 추가
        formData.append('image', imageFile);



        // AJAX 요청
        $.ajax({
            url: '/api/pipe/pipe',
            type: 'POST',
            data: formData,
            processData: false,  // 필수: FormData 처리 방지
            contentType: false,  // 필수: Content-Type 헤더 자동 설정
            
            success: function (response) {
                $('#result').text(`${response.label} : ${(response.confidence * 100).toFixed(2)}%`);
                if (response.label === '불량품') {
                    
                    Swal.fire({ 
                        title: '<span style="color: red;">불량품</span> 입니다.',       // Alert 제목
                        text: $('#result').text(),                                     // Alert 내용
                        icon: 'warning',                                               // Alert 타입
                        timer: 3000,
                        timerProgressBar: true,
                        confirmButtonText: '확인',
                        customClass: {
                            timerProgressBar: 'timer-bar'
                        }
                    });
                    
                } else {
                    $('#result').css('color', 'green');
                }


            },
            error: function (xhr) {
                const errorMsg = xhr.responseJSON?.error || '요청 처리 중 오류가 발생했습니다.';
                $('#result').text(`Error: ${errorMsg}`);
            }
        });
    });
});
