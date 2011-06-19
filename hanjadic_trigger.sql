CREATE VIRTUAL TABLE `hanjas` USING fts4(
  `hanja` text,
  `hangul` text,
  `part_of_speech` text,
  `english` text,
  `sajasongoh` boolean,
  extra_index text
);

INSERT INTO `hanjas` VALUES ('牽牛星','견우성','n','Altair',NULL);
INSERT INTO `hanjas` VALUES ('兩棲類','양서류','n','Amphibia',NULL);
INSERT INTO `hanjas` VALUES ('北氷洋','북빙양','n','Arctic Ocean',NULL);
