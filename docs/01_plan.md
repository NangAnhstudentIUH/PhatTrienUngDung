## 1. TỔNG QUAN ĐỀ TÀI
### 1.1 Kế Hoạch
Dưới đây là kế hoạch thực hiện đề tài xây dựng trang web đọc báo, áp dụng mô hình phát triển tăng trưởng (iterative development), cho phép cải tiến dần dần qua từng giai đoạn. Quy trình này được chia thành các giai đoạn chính với mốc thời gian cụ thể:

#### Giai đoạn 1: Phân tích Yêu cầu và Thiết kế Sơ bộ
**Thời gian**: 21/04 - 28/04
- **Phân tích yêu cầu**: Tìm hiểu những trang web đọc báo, phân tích để thu thập yêu cầu về tính năng và giao diện người dùng.
- **Thiết kế sơ bộ**: Tạo bản mẫu thiết kế sơ bộ cho trang web bao gồm wireframes và thiết kế cơ bản.

#### Giai đoạn 2: Phát triển Phiên bản Đầu tiên
**Thời gian**: 28/04 - 05/05
- **Xây dựng cơ bản**: Phát triển các tính năng cốt lõi như đăng nhập, xem bài viết.
- **Kiểm thử**: Thực hiện kiểm thử các chức năng

#### Giai đoạn 3: Phát triển và Mở rộng
**Thời gian**: 05/05 - 12/05
- **Phát triển tính năng**: Thêm tính năng tìm kiếm, lọc bài viết và cá nhân hóa nội dung.
- **Kiểm thử và tối ưu hóa**: Tiếp tục kiểm thử và cải tiến hiệu suất trang web.

#### Giai đoạn 4: Phát triển Tính năng Quản trị
**Thời gian**: 12/05 - 19/05
- **Quản lý nội dung và người dùng**: Phát triển giao diện quản lý cho admin để xét duyệt bài viết và quản lý người dùng.
- **Báo cáo và phân tích**: Tích hợp công cụ phân tích để theo dõi các chỉ số sử dụng trang web.

#### Giai đoạn 5: Tối ưu và Chuẩn bị Hoàn thành
**Thời gian**: 19/05 - 26/05
- **Kiểm thử cuối cùng**: Thực hiện kiểm thử toàn diện để đảm bảo mọi tính năng hoạt động trơn tru.

#### Giai đoạn 6: Phát triển và Cập nhật Liên tục
**Thời gian**: Tháng 5 trở đi
- **Phát triển liên tục**: Thêm các tính năng mới và cập nhật dựa trên yêu cầu thị trường và phản hồi người dùng.
- **Đánh giá và cải tiến**: Đánh giá hiệu quả sử dụng trang web, thực hiện cải tiến để đáp ứng nhu cầu ngày càng cao của người dùng.

### 1.2. Mô tả ý tưởng đề tài

Chúng tôi mong muốn xây dựng một website đọc báo bao gồm các tính năng chính sau:

 1. **Cập Nhật Tin Tức Thời Gian Thực:** Website cung cấp tin tức cập nhật liên tục từ nhiều nguồn uy tín và đa dạng, tự động phân loại tin tức theo chủ đề.

 1. **Giao Diện Thân Thiện:** Đảm bảo trải nghiệm người dùng mượt mà trên cả máy tính và điện thoại di động, với thiết kế responsive tương thích với mọi kích cỡ màn hình.

 1. **Tùy Chỉnh Người Dùng:** Người dùng có thể tùy chỉnh giao diện và loại tin tức họ muốn theo dõi, từ chính trị, kinh tế đến thể thao, giải trí.

 1. **Quản lý người dùng:** Có khả năng xem, thêm, xóa, hoặc cấm người dùng từ hệ thống.

 1. **Quản lý nội dung:** Xét duyệt và quản lý các bài đăng từ tác giả, chỉnh sửa nội dung nếu cần.

 1. **Báo cáo và Phân tích:** Truy cập vào bảng điều khiển để xem các số liệu thống kê như số lượng người dùng đăng ký mới, số lượt xem bài viết, tương tác người dùng, v.v.

 1. **Thống kê bài viết:** Xem số liệu về số lượt xem, bình luận, và chia sẻ của các bài viết mình đăng.

 1. **Phản hồi từ Admin:** Nhận xét, phản hồi từ admin về các bài viết để cải thiện chất lượng nội dung.

 1. **Hỗ trợ từ Admin:** Tác giả có thể yêu cầu sự hỗ trợ kỹ thuật hoặc chỉnh sửa nội dung từ admin để tối ưu hóa bài viết.

### 1.3. Sản phẩm MVP

1. Giao diện xem tin tức:
 - Hiển thị các bài viết theo danh mục như Thời sự, Kinh doanh, Công nghệ, v.v.
 - Bài viết được tổ chức theo độ mới và mức độ phổ biến.
 - Người dùng có thể nhấp vào mỗi tiêu đề để đọc toàn bộ bài viết.
2. Chức năng tìm kiếm:
 - Cung cấp khả năng tìm kiếm bài viết theo từ khóa.
 - Có thể lọc kết quả tìm kiếm theo ngày tháng hoặc danh mục.

### 1.4. Sản phẩm hoàn thiện

Dưới đây là chi tiết về sản phẩm hoàn thiện:

#### 1.4.1. Tính năng cho Người dùng (User)
- Hoàn thiện các chức năng cơ bản của web đọc báo như đăng ký/đăng nhập, đọc báo.

#### 1.4.2. Tính năng cho Tác giả (Author)
- Tác giả có thể theo dõi thống kê về số bài báo mà mình viết

#### 1.4.3. Tính năng cho Quản trị viên (Admin)
-  **Quản lý nội dung toàn diện**: Quản trị viên có quyền kiểm duyệt và chỉnh sửa bài viết và xóa nội dung không phù hợp.
- **Phân tích dữ liệu và báo cáo**: Truy cập vào các báo cáo chi tiết về lượt truy cập, tương tác người dùng, và hiệu suất bài viết để đưa ra quyết định chiến lược.

#### 1.4.4. Các tính năng bổ sung
- **Chức năng tóm tắt bài báo**: Giúp người đọc có thể đọc báo nhanh hơn mà không bị mất thông tin