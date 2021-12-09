-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 09, 2021 at 02:48 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbe_final_project_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `accesscard`
--

CREATE TABLE `accesscard` (
  `IdAccess` varchar(11) NOT NULL,
  `IdFasilitas1` varchar(11) NOT NULL,
  `IdFasilitas2` varchar(11) NOT NULL,
  `IdFasilitas3` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `fasilitas`
--

CREATE TABLE `fasilitas` (
  `IdFasilitas` varchar(11) NOT NULL,
  `Nama` varchar(30) NOT NULL,
  `JamBuka` time NOT NULL,
  `JamTutup` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `kendaraan`
--

CREATE TABLE `kendaraan` (
  `NoPlat` varchar(10) NOT NULL,
  `JenisKendaraan` text NOT NULL,
  `Warna` varchar(20) NOT NULL,
  `IdParkir` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `owner`
--

CREATE TABLE `owner` (
  `IdOwner` varchar(4) NOT NULL,
  `Nama` varchar(30) NOT NULL,
  `TempatLahir` varchar(30) NOT NULL,
  `TanggalLahir` date NOT NULL,
  `Kelamin` text NOT NULL,
  `Telepon` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `parkir`
--

CREATE TABLE `parkir` (
  `IdParkir` varchar(10) NOT NULL,
  `Lantai` int(11) NOT NULL,
  `Block` int(11) NOT NULL,
  `No` int(11) NOT NULL,
  `status` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `unit`
--

CREATE TABLE `unit` (
  `NoUnit` varchar(6) NOT NULL,
  `Tipe` varchar(10) NOT NULL,
  `Luas` int(11) NOT NULL,
  `IdOwner` varchar(4) NOT NULL,
  `IdAksesCard1` varchar(10) NOT NULL,
  `IdAksesCard2` varchar(10) NOT NULL,
  `IdAksesCard3` varchar(10) NOT NULL,
  `IdAksesCard4` varchar(10) NOT NULL,
  `IdAksesCard5` varchar(10) NOT NULL,
  `IdKendaraan1` varchar(10) NOT NULL,
  `IdKendaraan2` varchar(10) NOT NULL,
  `IdKendaraan3` varchar(10) NOT NULL,
  `IdKendaraan4` varchar(10) NOT NULL,
  `IdKendaraan5` varchar(10) NOT NULL,
  `IuranStatus` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `IdUser` varchar(3) NOT NULL,
  `Nama` varchar(30) NOT NULL,
  `Pass` varchar(30) NOT NULL,
  `Role` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`IdUser`, `Nama`, `Pass`, `Role`) VALUES
('1', 'fata2', '123', 'Admin'),
('2', 'hanz', '123', 'Admin'),
('3', 'fathi', '123', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accesscard`
--
ALTER TABLE `accesscard`
  ADD PRIMARY KEY (`IdAccess`),
  ADD KEY `IdAccess` (`IdAccess`),
  ADD KEY `IdFasilitas1` (`IdFasilitas1`),
  ADD KEY `IdFasilitas2` (`IdFasilitas2`),
  ADD KEY `IdFasilitas3` (`IdFasilitas3`);

--
-- Indexes for table `fasilitas`
--
ALTER TABLE `fasilitas`
  ADD PRIMARY KEY (`IdFasilitas`),
  ADD KEY `IdFasilitas` (`IdFasilitas`);

--
-- Indexes for table `kendaraan`
--
ALTER TABLE `kendaraan`
  ADD PRIMARY KEY (`NoPlat`),
  ADD KEY `NoPlat` (`NoPlat`),
  ADD KEY `IdParkir` (`IdParkir`);

--
-- Indexes for table `owner`
--
ALTER TABLE `owner`
  ADD PRIMARY KEY (`IdOwner`),
  ADD KEY `IdOwner` (`IdOwner`);

--
-- Indexes for table `parkir`
--
ALTER TABLE `parkir`
  ADD PRIMARY KEY (`IdParkir`),
  ADD KEY `IdParkir` (`IdParkir`);

--
-- Indexes for table `unit`
--
ALTER TABLE `unit`
  ADD PRIMARY KEY (`NoUnit`),
  ADD KEY `NoUnit` (`NoUnit`),
  ADD KEY `IdOwner` (`IdOwner`),
  ADD KEY `IdAksesCard1` (`IdAksesCard1`),
  ADD KEY `IdAksesCard2` (`IdAksesCard2`),
  ADD KEY `IdAksesCard3` (`IdAksesCard3`),
  ADD KEY `IdAksesCard4` (`IdAksesCard4`),
  ADD KEY `IdAksesCard5` (`IdAksesCard5`),
  ADD KEY `IdKendaraan1` (`IdKendaraan1`),
  ADD KEY `IdOwner_2` (`IdOwner`),
  ADD KEY `IdKendaraan2` (`IdKendaraan2`),
  ADD KEY `IdKendaraan3` (`IdKendaraan3`),
  ADD KEY `IdKendaraan4` (`IdKendaraan4`),
  ADD KEY `IdKendaraan5` (`IdKendaraan5`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`IdUser`),
  ADD KEY `IdUser` (`IdUser`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accesscard`
--
ALTER TABLE `accesscard`
  ADD CONSTRAINT `fasilitas1` FOREIGN KEY (`IdFasilitas1`) REFERENCES `fasilitas` (`IdFasilitas`),
  ADD CONSTRAINT `fasilitas2` FOREIGN KEY (`IdFasilitas2`) REFERENCES `fasilitas` (`IdFasilitas`),
  ADD CONSTRAINT `fasilitas3` FOREIGN KEY (`IdFasilitas3`) REFERENCES `fasilitas` (`IdFasilitas`);

--
-- Constraints for table `kendaraan`
--
ALTER TABLE `kendaraan`
  ADD CONSTRAINT `parkir` FOREIGN KEY (`IdParkir`) REFERENCES `parkir` (`IdParkir`);

--
-- Constraints for table `owner`
--
ALTER TABLE `owner`
  ADD CONSTRAINT `owner` FOREIGN KEY (`IdOwner`) REFERENCES `unit` (`IdOwner`);

--
-- Constraints for table `unit`
--
ALTER TABLE `unit`
  ADD CONSTRAINT `aksescard1` FOREIGN KEY (`IdAksesCard1`) REFERENCES `accesscard` (`IdAccess`),
  ADD CONSTRAINT `aksescard2` FOREIGN KEY (`IdAksesCard2`) REFERENCES `accesscard` (`IdAccess`),
  ADD CONSTRAINT `aksescard3` FOREIGN KEY (`IdAksesCard3`) REFERENCES `accesscard` (`IdAccess`),
  ADD CONSTRAINT `aksescard4` FOREIGN KEY (`IdAksesCard4`) REFERENCES `accesscard` (`IdAccess`),
  ADD CONSTRAINT `aksescard5` FOREIGN KEY (`IdAksesCard5`) REFERENCES `accesscard` (`IdAccess`),
  ADD CONSTRAINT `parkir1` FOREIGN KEY (`IdKendaraan1`) REFERENCES `kendaraan` (`NoPlat`),
  ADD CONSTRAINT `parkir2` FOREIGN KEY (`IdKendaraan2`) REFERENCES `kendaraan` (`NoPlat`),
  ADD CONSTRAINT `parkir3` FOREIGN KEY (`IdKendaraan3`) REFERENCES `kendaraan` (`NoPlat`),
  ADD CONSTRAINT `parkir4` FOREIGN KEY (`IdKendaraan4`) REFERENCES `kendaraan` (`NoPlat`),
  ADD CONSTRAINT `parkir5` FOREIGN KEY (`IdKendaraan5`) REFERENCES `kendaraan` (`NoPlat`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
