-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 29, 2020 at 07:26 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tinder`
--

-- --------------------------------------------------------

--
-- Table structure for table `proposals`
--

CREATE TABLE `proposals` (
  `proposal_id` int(11) NOT NULL,
  `romeo_id` int(11) NOT NULL,
  `juliet_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `proposals`
--

INSERT INTO `proposals` (`proposal_id`, `romeo_id`, `juliet_id`) VALUES
(1, 1, 2),
(2, 13, 2),
(3, 13, 4),
(4, 11, 14),
(5, 2, 1),
(6, 14, 11),
(7, 1, 3),
(8, 1, 4),
(9, 1, 10),
(10, 3, 4),
(11, 4, 3),
(12, 15, 1),
(13, 15, 6),
(14, 15, 12),
(15, 11, 15),
(16, 11, 2),
(17, 1, 15),
(18, 1, 16),
(19, 1, 17),
(20, 2, 6),
(21, 2, 7),
(22, 2, 9),
(23, 3, 2),
(24, 3, 14),
(25, 3, 15),
(26, 3, 17),
(27, 5, 4),
(28, 5, 7),
(29, 5, 10),
(30, 5, 14),
(31, 5, 15),
(32, 5, 16),
(33, 5, 17),
(34, 6, 16),
(35, 7, 17),
(36, 7, 16),
(37, 8, 15),
(38, 9, 10),
(39, 10, 9),
(40, 17, 7);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `bg` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `bio` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `fname`, `email`, `password`, `age`, `gender`, `bg`, `city`, `bio`) VALUES
(1, 'Salman Khan', 'bhai@gmail.com', 'katrina', 54, 'Male', 'salman.jpg', 'Mumbai', 'Being Human.....'),
(2, 'Katrina Kaif', 'behen@gmail.com', 'ranbir', 35, 'Female', 'katrina.jpg', 'Mumbai', 'Being arrogant.....'),
(3, 'Virat Kohli', 'virat@gmail.com', '1234', 31, 'Male', 'virat.jpg', 'Delhi', 'yooo'),
(4, 'Anushka Sharma', 'anushka@gmail.com', '12345', 30, 'Female', 'avatar.jpg', 'Mumbai', 'Actress'),
(5, 'Ravi Shastri', 'shashravi@gmail.com', 'ravi123', 52, 'Male', 'ravi.jpg', 'Kolkata', 'Cricket Coach'),
(6, 'Varun Dhawan', 'dhawan@gmail.com', 'alia', 25, 'Male', 'Avatar.jpg', 'Delhi', 'Josh Actor..........'),
(7, 'K. Lokesh Rahul', 'rahulkl@gmail.com', 'KlRahul', 23, 'Male', 'Avatar.jpg', 'Delhi', 'Cricket is lyfff.............'),
(8, 'Ram Sanyal', 'ramsan@gmail.com', 'sanyal', 21, 'Male', 'Avatar.jpg', 'Lucknow', 'Getting desperate......'),
(9, 'Akshay Kumar', 'akshay@gmail.com', 'gabbar', 47, 'Male', 'Avatar.jpg', 'Mumbai', '.....Swag.....'),
(10, 'Raveena Tandon', 'tandon@gmail.com', 'akshay', 39, 'Female', 'Avatar.jpg', 'Jammu', 'Dance.....||.....Dance.......'),
(11, 'INDRAJIT AKULI', 'indra.akuli.1999@gmail.com', 'Indrajit123#', 20, 'Male', 'Avatar.jpg', 'Newtown', 'On the way to be an Engineer...'),
(12, 'Sudipta Pal', 'sudipta550@outlook.com', 'shilpa', 21, 'Male', 'Avatar.jpg', 'Goghat', 'Superman'),
(13, 'ATANU MANNA', 'atanu8357@gmail.com', 'atanu8357', 28, 'Male', 'Avatar.jpg', 'Midnapore', 'dome balobashbo re!'),
(14, 'Ananya Roy', 'ananya14feb@gmail.com', 'mishti', 20, 'Female', 'Avatar.jpg', 'Chandannagar', 'Mishtiii...'),
(15, 'Deepika  Padukone', 'padukone@gmail.com', 'Ranveer', 31, 'Female', 'Avatar.jpg', 'Karnataka', 'Jindegi na milegi doobara'),
(16, 'Ananya Pandey', 'pandey@gmail.com', '12345', 21, 'Female', 'Avatar.jpg', 'Mumbai', 'Struggling..........'),
(17, 'Sania Mirza', 'mirza@gmail.com', 'mirza123', 34, 'Female', 'Avatar.jpg', 'Hydrabad', 'Tennis Player');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `proposals`
--
ALTER TABLE `proposals`
  ADD PRIMARY KEY (`proposal_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `proposals`
--
ALTER TABLE `proposals`
  MODIFY `proposal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
