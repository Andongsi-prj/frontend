$(document).ready(function() {
    const defectivePipe = "bad_pipe.jpg"; // 불량품 파일명
    let belt = $(".belt");

    function checkDefectivePipe() {
        $(".belt img").each(function() {
            if ($(this).attr("src").includes(defectivePipe)) {
                belt.css("animation", "none"); // 애니메이션 중지
                clearInterval(beltChecker); // 검사 중지
                
                Swal.fire({
                    icon: 'warning',
                    title: '불량품 감지!',
                    text: '컨베이어 벨트를 멈춥니다.',
                    confirmButtonText: '확인',
                    timer: 3000,
                    timerProgressBar: true,
                    customClass: {
                        timerProgressBar: 'timer-bar'
                    }
                }).then(() => {
                    // 알림창이 닫힌 후 실행될 코드
                    belt.css("animation", ""); // 애니메이션 재시작
                    beltChecker = setInterval(checkDefectivePipe, 2000); // 검사 재시작
                });
                
                return false;
            }
        });
    }

    // 일정 시간마다 불량품 검사 실행
    // let beltChecker = setInterval(checkDefectivePipe, 2000);
});
