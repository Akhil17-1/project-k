// src/components/Header.js
import React from 'react';
import styled from 'styled-components';
import { FaBars, FaUserCircle } from 'react-icons/fa';

const HeaderContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #141414;
  color: white;
`;

const Title = styled.h1`
  margin: 0;
`;

const Icon = styled.div`
  cursor: pointer;
`;

const Header = ({ toggleMenu }) => {
  return (
    <HeaderContainer>
      <Icon onClick={toggleMenu}>
        <FaBars size={24} />
      </Icon>
      <Title>Project K</Title>
      <Icon>
        <FaUserCircle size={24} />
      </Icon>
    </HeaderContainer>
  );
};

export default Header;
