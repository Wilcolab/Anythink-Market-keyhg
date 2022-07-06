import React from "react";
import logo from "../../imgs/logo.png";
import agent from "../../agent";

const Banner = (props) => {
  const handleChange = (ev) => {
    ev.preventDefault();
    const title = ev.target.value;
    if (title.length > 2) {
      props.onItemSearch(
        title,
        (page) => agent.Items.byTitle(title, page),
        agent.Items.byTitle(title)
      );
    }
  };

  return (
    <div className="banner text-white">
      <div className="container p-4 text-center">
        <img src={logo} alt="banner" />
        <div>
          <span id="get-part">A place to get</span>
          <input id="search-box" className="rounded-pill m-2 pt-2 pb-2 pl-3 pr-3 w-50" placeholder="What is it that you truly desire?" type="text" onChange={handleChange}></input>
          <i className="ion-search"></i>
          <span> the cool stuff.</span>          
        </div>
      </div>
    </div>
  );
};

export default Banner;
