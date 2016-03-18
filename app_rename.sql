update django_content_type set app_label = 'travel' where app_label = 'me' ;
rename table `me_category` to `travel_category` ;
rename table `me_city` to `travel_city`;
rename table `me_country` to `travel_country`;
rename table `me_post` to `travel_post`;
rename table `me_post_cities` to `travel_post_cities`;
rename table `me_post_tags` to `travel_post_tags`;
rename table `me_postmap` to `travel_postmap`;
rename table `me_postphoto` to `travel_postphoto`;
rename table `me_tag` to `travel_tag`;
rename table `me_user` to `travel_user`;
rename table `me_user_groups` to `travel_user_groups`;
rename table `me_user_user_permissions` to `travel_user_user_permissions`;
update django_migrations set app = 'travel' where app = 'me' ;
drop table `south_migrationhistory` ;
drop table `adminfiles_fileuploadreference` ;
drop table `adminfiles_fileupload` ;

