import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';

const ThumbnailContainer = styled.div`
  width: 200px;
  margin: 10px;
  background-color: #222;
  color: white;
  border-radius: 5px;
  overflow: hidden;
  cursor: pointer;
  text-decoration: none;

  img {
    width: 100%;
    height: 150px;
    object-fit: cover;
  }

  div {
    padding: 10px;
  }
`;

const Thumbnail = ({ title, image, link }) => {
  return (
    <Link to={link}>
      <ThumbnailContainer>
        <img src={image} alt={title} />
        <div>
          <h4>{title}</h4>
        </div>
      </ThumbnailContainer>
    </Link>
  );
};

export default Thumbnail;
