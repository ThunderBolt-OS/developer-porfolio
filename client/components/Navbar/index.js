import React from 'react'
import styles from './styles.module.scss'
import { FaBars } from 'react-icons/fa'

const Navbar = () => {
  return (
    <div className={styles.container}>
      
      <div className={styles.navbar}>

        <div className={styles.title}>
          <div className={styles.logo}>ThunderBolt</div>          
        </div> 

        <div className={styles.navlinks}>
          <ul className={styles.ul}>
            <li className={styles.li}> <span>1.0</span> About Me</li>
            <li className={styles.li}> <span>2.0</span> Experience</li>
            <li className={styles.li}> <span>3.0</span> Projects</li>
            <li className={styles.li}> <span>4.0</span> Testimonials</li>
            <li className={styles.li}> <span>5.0</span> Contact Me</li>
          </ul>
        </div>
      </div>

    </div>
  )
}

export default Navbar;